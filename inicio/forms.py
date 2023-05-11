from django import forms
from inicio.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'})
        }