# Generated by Django 4.1.2 on 2023-03-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_itempedido_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('fecha_listo', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estado', models.PositiveIntegerField(default=1)),
                ('items', models.ManyToManyField(blank=True, to='pedidos.itempedido')),
            ],
        ),
    ]
