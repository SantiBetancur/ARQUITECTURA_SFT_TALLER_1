from django import forms
from register_page.models import Seller

class UserForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Local Market','autocomplete':'new-username'}))
    email = forms.CharField(label="",    widget=forms.TextInput(attrs={'placeholder':'localmarket@email.com','autocomplete':'new-email'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Al menos 6 carácteres', 'minlength': '6'}))
    password_confirmation = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Escribe la misma contraseña', 'minlength': '6'}))

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller   
        fields = "__all__"

   