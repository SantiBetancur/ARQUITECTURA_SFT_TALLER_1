from django import forms

class UserForm(forms.Form):
        username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Local Market','autocomplete':'new-username'}))
        email = forms.CharField(label="",    widget=forms.TextInput(attrs={'placeholder':'localmarket@email.com','autocomplete':'new-email'}))
        password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Al menos 6 carácteres, No llenes este campo si no quieres cambiar la contraseña', 'minlength': '6'}), required=False)
        password_confirmation = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Confirma la contraseña', 'minlength': '6'}), required=False)