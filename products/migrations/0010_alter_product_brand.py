# Generated by Django 3.2.9 on 2021-11-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Mikrotik', 'Mikrotik'), ('TPLink', 'TPLink'), ('HPE', 'HPE'), ('Unifi', 'Unifi'), ('Draytek', 'Draytek'), ('Camera', 'Camera'), ('Other', 'Other')], default='Other', max_length=100),
        ),
    ]