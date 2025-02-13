from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
  return render(request, 'users/home.html')

@login_required
def autenticated(request):
  return render(request, 'users/autenticated.html')

def login_view(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('autenticated')
    else:
      return render(request, 'users/login.html', {'error': 'Invalid username and password'})
  return render(request, 'users/login.html')

def logout_view(request):
  logout(request)
  return redirect('login')

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('autenticated')
    else:
      return render(request, 'users/signup.html', {'form': form})
  else:
    form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})