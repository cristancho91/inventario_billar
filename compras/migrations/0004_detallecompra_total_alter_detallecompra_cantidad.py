# Generated by Django 4.2.4 on 2023-10-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0003_alter_compra_options_remove_compra_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallecompra',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='detallecompra',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]
