from django import forms
from register_page.models import Seller

class UserForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Local Market','autocomplete':'new-username'}))
    email = forms.CharField(label="",    widget=forms.TextInput(attrs={'placeholder':'algo@email.com','autocomplete':'new-email'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Debe tener al menos una: mayúscula, minúscula y número','autocomplete':'new-password'}))
    password_confirmation = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Confirmación','autocomplete':'new-password'}))

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller   
        fields = "__all__"

   