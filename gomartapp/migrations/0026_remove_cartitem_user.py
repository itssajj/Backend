# Generated by Django 4.2.6 on 2023-10-22 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0025_remove_usermessage_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
    ]
