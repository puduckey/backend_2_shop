from django import forms
from inicio.models import Producto
from .models import Valorizacion

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'categoria': forms.Select(attrs={'class': 'form-control'})
        }

class ValorizacionForm(forms.ModelForm):
    class Meta:
        model = Valorizacion
        fields = ['producto', 'valoracion', 'comentario', 'autor']
        widgets = {
            'producto': forms.Select(attrs={'class': 'form-control'}),
            'valoracion': forms.Select(attrs={'class': 'form-select'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
        }