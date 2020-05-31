# Generated by Django 3.0.6 on 2020-05-31 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(through='relacion.CarritoProducto', to='relacion.Producto'),
        ),
    ]