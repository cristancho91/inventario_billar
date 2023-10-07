# Generated by Django 4.2.4 on 2023-10-06 21:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_producto_stock'),
        ('clientes', '0001_initial'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ventas',
            options={'verbose_name': 'venta', 'verbose_name_plural': 'ventas'},
        ),
        migrations.AddField(
            model_name='ventas',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.clientes'),
        ),
        migrations.AddField(
            model_name='ventas',
            name='codigo',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventas',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventas',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('total', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.ventas')),
            ],
            options={
                'verbose_name': 'detalleVenta',
                'verbose_name_plural': 'detalleVentas',
            },
        ),
        migrations.AddField(
            model_name='ventas',
            name='producto',
            field=models.ManyToManyField(related_name='detalle_venta', through='ventas.DetalleVenta', to='productos.producto'),
        ),
        migrations.AddField(
            model_name='ventas',
            name='tipo_pago',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ventas.tipopago'),
            preserve_default=False,
        ),
    ]