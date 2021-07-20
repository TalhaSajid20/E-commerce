from django.forms import ModelForm
from store.models.product import Product

class ProductForm(ModelForm):
     class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'image', 'description']