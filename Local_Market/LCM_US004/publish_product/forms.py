from django import forms
from community_main_page.models import products

class ProductForm(forms.ModelForm):

    class Meta:
        model = products
        fields = ['name', 'price', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['id'] = 'price-input'

class Image_prompt_form(forms.Form):
    user_image_prompt = forms.CharField(label='prompt', widget=forms.TextInput(attrs={'placeholder': 'Personas Felices comiendo galletas en la playa'}))
