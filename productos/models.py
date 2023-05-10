from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    ingredientes = models.ManyToManyField('Ingrediente', related_name='productos', blank=True)

    def __str__(self):
        return self.nombre