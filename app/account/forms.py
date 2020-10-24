from django import forms
from django.contrib.auth import get_user_model


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput
        (attrs={'class': 'text', 'name': 'Username', 'placeholder': 'Username'}))

    email = forms.EmailField(widget=forms.EmailInput
        (attrs={'class': 'text email', 'name': 'email', 'placeholder': 'Email'}))

    password = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'text password', 'name': 'password', 'placeholder': 'Password'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput
        (attrs={'class': 'text email', 'name': 'email', 'placeholder': 'Email'}))

    password = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'text password', 'name': 'password', 'placeholder': 'Password'}))
