# Generated by Django 4.2.6 on 2023-10-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0027_cartitem_user_alter_cartitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cartuser',
            field=models.CharField(default='Tomi', max_length=100),
        ),
    ]
