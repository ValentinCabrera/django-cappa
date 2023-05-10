from django.contrib import admin
from .models import Producto, Categoria, Ingrediente

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria')

# Register your models here.
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria)
admin.site.register(Ingrediente)