# Generated by Django 4.1.2 on 2023-03-18 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_alter_pedido_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itempedido',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='subtotal',
        ),
    ]
