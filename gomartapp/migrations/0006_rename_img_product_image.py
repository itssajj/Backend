# Generated by Django 4.2.5 on 2023-09-06 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0005_alter_product_img_alter_product_img1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
    ]