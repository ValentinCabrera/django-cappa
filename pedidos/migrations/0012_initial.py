# Generated by Django 4.1.2 on 2023-03-18 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productos', '0003_remove_ingrediente_imagen_categoria_imagen'),
        ('pedidos', '0011_delete_itempedido_delete_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='pedidos.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='productos.producto')),
            ],
        ),
    ]