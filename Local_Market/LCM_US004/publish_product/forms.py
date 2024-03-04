from django import forms
from community_main_page.models import products

class ProductForm(forms.ModelForm):

    class Meta:
        model = products
        fields = ['name', 'price', 'description', 'image', 'rating']


    name = forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control'}), max_length=50)    
    price = forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control'}), max_length=10)
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'forms-control'}), max_length=250)
    image = forms.ImageField(label = 'Avatar', required=False, widget=forms.FileInput(attrs = {'class':'forms-control'}))
    rating = forms.IntegerField(widget=forms.TextInput(attrs={'class':'forms-control'}))