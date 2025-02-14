from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import EmailAuthenticationForm, CustomUserCreationForm


@login_required
def autenticated(request):
  return render(request, 'users/autenticated.html')

def login_view(request):
  if request.method == 'POST':
    form = EmailAuthenticationForm(request, request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('autenticated')
  else:
    form = EmailAuthenticationForm()
  return render(request, 'users/login.html', {'form': form})

def logout_view(request):
  logout(request)
  return redirect('login')

def signup_view(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('autenticated')
    else:
      return render(request, 'users/signup.html', {'form': form})
  else:
    form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})