from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['nome', 'Descrição', 'tipo', 'status', 'obs_status', 'valor', 'Especificação', 'foto']
