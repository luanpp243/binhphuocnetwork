# Generated by Django 3.2.9 on 2021-11-07 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211107_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Mikrotik', 'Mikrotik'), ('TPLink', 'TPLink'), ('HPE', 'HPE'), ('Unifi', 'Unifi'), ('Camera', 'Camera'), ('Other', 'Other')], default='Other', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='classify',
            field=models.CharField(choices=[('Router', 'Router'), ('Wifi', 'Wifi'), ('Camera', 'Camera'), ('Switch/Hub', 'Switch/Hub'), ('Other', 'Other')], default='Other', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Còn hàng', 'Còn hàng'), ('Hết hàng', 'Hết hàng'), ('Othe', 'Other')], default='Còn hàng', max_length=100),
        ),
    ]
