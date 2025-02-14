# Autenticação de Usuários com Email no Django

Este guia fornece um passo a passo para implementar autenticação de usuários utilizando email em um projeto Django.

## Pré-requisitos

- Python instalado
- Django instalado (`pip install django`)
- Projeto Django criado

## Passos

### 1. Configurar o Projeto

Crie um novo projeto Django ou utilize um existente:

```bash
django-admin startproject myproject
cd myproject
```

### 2. Criar um App

Crie um novo app para gerenciar a autenticação:

```bash
python manage.py startapp users
```

Adicione o app `users` ao seu `INSTALLED_APPS` no arquivo `settings.py`:

```python
INSTALLED_APPS = [
  ...
  'users',
]
```

### 3. Modelar o Usuário

Crie um modelo de usuário personalizado em `users/models.py`:

```python
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyUserManager(BaseUserManager):
  def create_user(self, email, password=None, **extra_fields):
    if not email:
      raise ValueError('O email deve ser fornecido')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser):
  email = models.EmailField(unique=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)

  objects = MyUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.email
```

### 4. Atualizar Configurações

Atualize o arquivo `settings.py` para usar o modelo de usuário personalizado:

```python
AUTH_USER_MODEL = 'users.MyUser'
```

### 5. Criar e Aplicar Migrações

Crie e aplique as migrações para o novo modelo de usuário:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Formulários de Autenticação

Crie formulários de registro e login em `users/forms.py`:

```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MyUser

class UserRegisterForm(UserCreationForm):
  class Meta:
    model = MyUser
    fields = ['email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
  username = forms.EmailField(label='Email')
```

### 7. Views de Autenticação

Crie views para registro e login em `users/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, UserLoginForm

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
    form = UserLoginForm(request, data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('home')
  else:
    form = UserLoginForm()
  return render(request, 'users/login.html', {'form': form})
```

### 8. URLs

Adicione URLs para as views de autenticação em `users/urls.py`:

```python
from django.urls import path
from .views import register, login_view

urlpatterns = [
  path('register/', register, name='register'),
  path('login/', login_view, name='login'),
]
```

Inclua as URLs do app `users` no arquivo `urls.py` principal do projeto:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('users/', include('users.urls')),
]
```

### 9. Templates

Crie templates para registro e login em `users/templates/users/register.html` e `users/templates/users/login.html`:

**register.html**:

```html
<h2>Register</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Register</button>
</form>
```

**login.html**:

```html
<h2>Login</h2>
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
</form>
```

### 10. Testar a Implementação

Execute o servidor de desenvolvimento e teste a funcionalidade de registro e login:

```bash
python manage.py runserver
```

Acesse `http://127.0.0.1:8000/users/register/` para registrar um novo usuário e `http://127.0.0.1:8000/users/login/` para fazer login.

## Conclusão

Você implementou com sucesso a autenticação de usuários utilizando email em um projeto Django. Para mais personalizações, consulte a [documentação oficial do Django](https://docs.djangoproject.com/).