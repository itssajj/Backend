# Generated by Django 4.2.6 on 2023-10-18 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0017_cartitem_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]