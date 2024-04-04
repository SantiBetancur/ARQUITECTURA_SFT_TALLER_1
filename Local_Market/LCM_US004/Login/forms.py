from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Ingresa un nombre de usuario o un email','autocomplete':'new-username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Ingresa tu contraseña','autocomplete':'new-password'}))
