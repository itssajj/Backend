# Generated by Django 4.2.6 on 2023-10-24 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gomartapp', '0041_profile_firstname_profile_lastname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alaye',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alayeuser', models.CharField(default='Tomi', max_length=100)),
                ('location', models.CharField(default='Ellesse', max_length=100)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]