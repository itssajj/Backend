# Generated by Django 4.2.6 on 2023-10-23 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0028_cartitem_cartuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gomartfiles/static/'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]