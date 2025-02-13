# Sistema de Autenticação Simples em Django

Este documento descreve os passos para criar um sistema de autenticação simples utilizando Django.

## Pré-requisitos

- Python 3.x
- Django 3.x ou superior

## Passos

### 1. Criar um novo projeto Django

```bash
django-admin startproject sisgef
cd sisgef
```

### 2. Criar um novo aplicativo Django

```bash
python manage.py startapp users
```

### 3. Adicionar o aplicativo ao projeto

Edite o arquivo `settings.py` e adicione `users` à lista `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
  ...
  'users',
]
```

### 4. Configurar URLs

Edite o arquivo `sisgef/urls.py` para incluir as URLs do aplicativo `users`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('users/', include('users.urls')),
]
```

### 5. Criar URLs do aplicativo

Crie um arquivo `users/urls.py` e defina as URLs do aplicativo:

```python
from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('signup/', views.signup_view, name='signup'),
]
```

### 6. Criar as views

Edite o arquivo `users/views.py` para adicionar as views de login, logout e signup:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      return render(request, 'users/login.html', {'error': 'Invalid credentials'})
  return render(request, 'users/login.html')

def logout_view(request):
  logout(request)
  return redirect('home')

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
  else:
    form = UserCreationForm()
  return render(request, 'users/signup.html', {'form': form})
```

### 7. Criar templates

Crie os arquivos de template `login.html` e `signup.html` na pasta `users/templates/users/`.

**login.html**:

```html
<form method="post">
  {% csrf_token %}
  <label for="username">Username:</label>
  <input type="text" name="username" required>
  <label for="password">Password:</label>
  <input type="password" name="password" required>
  <button type="submit">Login</button>
  {% if error %}
    <p>{{ error }}</p>
  {% endif %}
</form>
```

**signup.html**:

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Sign Up</button>
</form>
```

### 8. Executar migrações

```bash
python manage.py migrate
```

### 9. Executar o servidor

```bash
python manage.py runserver
```

Agora você deve ter um sistema de autenticação simples funcionando em seu projeto Django.
