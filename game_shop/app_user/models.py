from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    balance = models.DecimalField(decimal_places=2, default=0, max_digits=100000, verbose_name='баланс')
    royalty = models.ForeignKey('Royalty', on_delete=models.SET_NULL, default='1', null=True,
                                verbose_name='статус пользователя', related_name='royalty')
    money_spent = models.DecimalField(default=0, decimal_places=2, max_digits=100000, verbose_name='потрачено денег')

    class Meta:
        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'профили пользователей'

    def __str__(self):
        return f'{self.user.username}'


class Royalty(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')
    image = models.ImageField(upload_to='royalty_status_images/', verbose_name='картинка')

    class Meta:
        verbose_name = 'статус пользователя'
        verbose_name_plural = 'статусы пользователей'

    def __str__(self):
        return f'{self.id}. {self.title}'
