# Generated by Django 4.2.5 on 2023-09-11 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0008_alter_product_category_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('SHIRT', 'SHIRT'), ('TROUSER', 'TROUSER'), ('SHORTS', 'SHORTS'), ('SNEAKER', 'SNEAKER'), ('CAP', 'CAP'), ('HOODIE', 'HOODIE'), ('TSHIRT', 'TSHIRT'), ('JERSEY', 'JERSEY'), ('CAP', 'CAP'), ('BELT', 'BELT'), ('SOCKS', 'SOCKS'), ('WATCHES', 'WATCHES'), ('N', 'NONE')], default='N', max_length=20),
        ),
    ]