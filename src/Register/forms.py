from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import *
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("__all__")
        exclude = ('username.help_text',)
        help_texts = {
            'username': None,
            'email': None,
            'password1':None,
            'password2':None,

        }
        
print(CustomUserCreationForm)       