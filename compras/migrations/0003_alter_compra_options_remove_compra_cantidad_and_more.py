# Generated by Django 4.2.4 on 2023-10-06 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_imagen'),
        ('proveedores', '0003_alter_proveedores_imagen'),
        ('compras', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compra',
            options={'verbose_name': 'compra', 'verbose_name_plural': 'compras'},
        ),
        migrations.RemoveField(
            model_name='compra',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='compra',
            name='producto',
        ),
        migrations.AlterField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proveedores.proveedores'),
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
            options={
                'verbose_name': 'detalleCompra',
                'verbose_name_plural': 'detalleCompras',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='producto',
            field=models.ManyToManyField(related_name='detalle_compra', through='compras.DetalleCompra', to='productos.producto'),
        ),
    ]
