from django import forms
from Login.models import LoginM

class LoginForm(forms.Form):
    class Meta:
        model = LoginM
        fields = ['username', 'password']

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control'}), max_length=20)
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control'}), max_length=15)