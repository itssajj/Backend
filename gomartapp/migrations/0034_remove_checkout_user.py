# Generated by Django 4.2.6 on 2023-10-24 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0033_alter_checkout_cartitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='user',
        ),
    ]
