from django import forms
from community_main_page.models import products


class ProductForm(forms.ModelForm):

    class Meta:
        model = products
        fields = ['name', 'price', 'description', 'image']
    image = forms.ImageField(label='Avatar', required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['id'] = 'price-input'

class Image_prompt_form(forms.Form):
    user_image_prompt = forms.CharField(label='prompt', widget=forms.TextInput(attrs={'placeholder': 'Brownie de chocolate servido en un plato de oro'}))
