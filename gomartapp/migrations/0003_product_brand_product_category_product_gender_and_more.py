# Generated by Django 4.2.5 on 2023-09-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0002_product_description_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Gucci', 'Gucci'), ('Nike', 'Nike'), ('Hublot', 'Hublot'), ('Northface', 'Northface'), ('Ellesse', 'Ellesse'), ('Balenciaga', 'Balenciaga'), ('vincero', 'vincero'), ('Vinchigo', 'Vinchigo'), ('Tommy Hilfiger', 'Tommy Hilfiger'), ('Jersy', 'Jersy'), ('Converse', 'Converse'), ('Prada', 'Prada'), ('N', 'None')], default='N', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('B', 'BLACK'), ('W', 'WHITE'), ('N', 'NONE')], default='N', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unisex'), ('B', 'BOY'), ('G', 'GIRL'), ('W', 'WATCHES')], default='U', max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=' New on gomart'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
