from django import forms
from community_main_page.models import products

class ProductForm(forms.ModelForm):

    class Meta:
        model = products
        fields = ['name', 'price', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['id'] = 'price-input'