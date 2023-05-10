from django.db import models
from productos.models import Producto
from django.utils import timezone

class Pedido(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def get_total(self):
        total = 0

        if self.id:
            for i in self.items.all():
                total += i.get_subtotal()
            
        return total
    
    get_total.short_description = 'Total'

    def minutos_transcurridos(self):
        tiempo_transcurrido = int((timezone.now() - self.fecha).total_seconds() / 30)
        return tiempo_transcurrido
    
    def get_color(self):
        tiempo = self.minutos_transcurridos()
        color = 255 - int(tiempo * 12.75)

        if color < 0:
            return 0

        return color

    
class ItemPedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='items')
    orden = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.pk:  # Nuevo objeto
            # Obtener el último número de orden
            last_orden = self.pedido.items.aggregate(models.Max('orden'))['orden__max']
            if last_orden is None:
                last_orden = 0

            self.orden = last_orden + 1

        super().save(*args, **kwargs)

    def aumentar_cantidad(self):
        self.cantidad += 1
        self.save()

    def disminuir_cantidad(self):
        if self.cantidad == 1:
            self.delete()
            return True

        else:
            self.cantidad -= 1
            self.save()

    def get_subtotal(self):
        subtotal = self.cantidad * self.producto.precio
        return subtotal
    
    get_subtotal.short_description = 'Subtotal'

    def __str__(self):
        return self.producto.nombre