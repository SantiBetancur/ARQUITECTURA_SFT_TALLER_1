from django import forms
from register_page.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control'}), max_length=20)
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control'}), max_length=30)
    password = forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control'}), max_length=15)