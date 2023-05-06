from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    img_url = models.URLField()
    def __str__(self):
        return self.name