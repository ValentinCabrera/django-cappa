# Generated by Django 4.1.2 on 2023-03-18 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_remove_itempedido_pedido_alter_itempedido_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itempedido',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
