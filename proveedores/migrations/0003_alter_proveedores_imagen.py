# Generated by Django 4.2.4 on 2023-10-05 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_alter_proveedores_nombre_contacto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='imagen',
            field=models.ImageField(blank=True, default='prov-defualt.png', null=True, upload_to='proveedores/img'),
        ),
    ]
