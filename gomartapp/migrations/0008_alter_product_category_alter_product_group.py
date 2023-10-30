# Generated by Django 4.2.5 on 2023-09-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0007_product_color_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('B', 'BLACK'), ('W', 'WHITE'), ('N', 'NEW'), ('N', 'NONE')], default='N', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('SHIRT', 'BLACK'), ('TROUSER', 'WHITE'), ('SHORTS', 'NEON'), ('SNEAKER', 'RED'), ('CAP', 'BLUE'), ('BROWN', 'BROWN'), ('TSHIRT', 'YELLOW'), ('JERSEY', 'GREY'), ('CAP', 'PINK'), ('BELT', 'GREEN'), ('SOCKS', 'ORANGE'), ('WATCHES', 'PURPLE'), ('N', 'NONE')], default='N', max_length=20),
        ),
    ]