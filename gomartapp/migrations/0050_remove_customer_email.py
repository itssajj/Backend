# Generated by Django 4.2.6 on 2023-10-25 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gomartapp', '0049_customer_email_customer_firstname_customer_lastname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
    ]