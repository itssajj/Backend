# Generated by Django 4.2.6 on 2023-10-16 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0015_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='quantity',
        ),
    ]
