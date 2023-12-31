# Generated by Django 4.2.6 on 2023-10-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0048_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='firstname',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(default='080', max_length=100),
        ),
    ]
