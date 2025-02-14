from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="E-mail")

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',) 