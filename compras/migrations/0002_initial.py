# Generated by Django 4.2.4 on 2023-10-05 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('proveedores', '0002_alter_proveedores_nombre_contacto_and_more'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.productoproveedor'),
        ),
    ]
