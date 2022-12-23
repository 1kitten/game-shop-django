from django.db import models


class Shop(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'магазин'
        verbose_name_plural = 'магазины'


class Item(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(max_length=1000, verbose_name='описание')
    price = models.DecimalField(max_digits=100000, decimal_places=2, verbose_name='цена')
    stock = models.IntegerField(verbose_name='остаток')
    picture = models.ImageField(upload_to='items_pictures/', null=True, blank=True, verbose_name='картинка')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        ordering = ['title']
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
