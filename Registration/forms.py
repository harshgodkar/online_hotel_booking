from django import forms
from .models import Registration

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('username', 'password', 'confirm_passwrd')
        