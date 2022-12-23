# Generated by Django 2.2 on 2022-12-18 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='money_spent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100000, verbose_name='потрачено денег'),
        ),
    ]
