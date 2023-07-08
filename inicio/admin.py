from django.contrib import admin
from inicio.models import Producto
from django.contrib import admin

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'marca', 'price', 'stock', 'img_url', 'categoria']

admin.site.register(Producto, ProductoAdmin)