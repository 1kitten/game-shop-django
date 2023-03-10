# Generated by Django 2.2 on 2022-12-18 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='наименование')),
            ],
            options={
                'verbose_name': 'магазин',
                'verbose_name_plural': 'магазины',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='наименование')),
                ('description', models.TextField(max_length=1000, verbose_name='описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=100000, verbose_name='цена')),
                ('stock', models.IntegerField(verbose_name='остаток')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='items_pictures/', verbose_name='картинка')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shop.Shop')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
    ]
