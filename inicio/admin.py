from django.contrib import admin
from inicio.models import Producto
from django.contrib import admin

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price', 'stock', 'img_url']

admin.site.register(Producto, ProductoAdmin)