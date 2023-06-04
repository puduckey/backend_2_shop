from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
#    marca = models.TextField()
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    img_url = models.URLField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    
# class Valorizacion(models.Model):
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     valoracion = models.IntegerField(choices=((1, '1 - Muy malo'), (2, '2 - Malo'), (3, '3 - Regular'), (4, '4 - Bueno'), (5, '5 - Excelente')))
#     comentario = models.TextField()
#     autor = models.CharField(max_length=50)
# 
#     def __str__(self):
#         return f"Valoración de {self.producto.name}"
