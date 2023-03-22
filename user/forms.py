from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction


class AdminRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')
        widgets={'username': forms.TextInput(attrs={'class': 'input', 'type':'text', 'placeholder':'UserName'}),
                 'email': forms.EmailInput(attrs={'class': 'input', 'type':'email', 'placeholder':'Email'}),
                 'password1': forms.PasswordInput(attrs={'class': 'input', 'type':'password', 'placeholder':'Password'}),
                 'password2': forms.PasswordInput(attrs={'class': 'input', 'type':'password', 'placeholder':'Repeat Password'})}

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        return user
    
class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2','gender')
        widgets={'username': forms.TextInput(attrs={'class': 'input', 'type':'text', 'placeholder':'UserName'}),
                 'email': forms.EmailInput(attrs={'class': 'input', 'type':'email', 'placeholder':'Email'}),
                 'password1': forms.PasswordInput(attrs={'class': 'input', 'type':'password', 'placeholder':'Password'}),
                 'password2': forms.PasswordInput(attrs={'class': 'input', 'type':'password', 'placeholder':'Repeat Password'}),
                 }

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_user = True
        user.save()
        return user
    


# class LoginForm(forms.ModelForm): 
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username','password')       
#         widgets={'username': forms.TextInput(attrs={'class': 'input', 'type':'text', 'placeholder':'UserName'}),
#                 'password': forms.PasswordInput(attrs={'class': 'input', 'type':'password', 'placeholder':'Password'})}


