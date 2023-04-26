from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.db import transaction

   
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        strip=False,
        widget=forms.TextInput,
    )
    email = forms.CharField(
        label="Email",
        strip=False,
        widget=forms.EmailInput,
    )
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Repeat Password",
        strip=False,
        widget=forms.PasswordInput,
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')
        widgets={'username': forms.TextInput(attrs={'class': 'input', 'type':'text', 'placeholder':'Username'}),
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
    


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(
        label="Username",
        strip=False,
        widget=forms.TextInput,
    )
    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','gender','qualification','bio','profilepic')

