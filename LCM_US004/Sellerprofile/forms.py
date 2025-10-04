from django import forms
from Sellerprofile.models import Seller

class SellerForm(forms.ModelForm):

    class Meta:
        model = Seller   
        fields = ['name', 'email', 'location', 'phone', 'age', 'description', 'photo', 'permission']



    photo = forms.ImageField(required=False)  
    permission = forms.FileField(required=False)    
    location = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'De lunes a viernes de 8 a 12 p.m en la cafetería'}))