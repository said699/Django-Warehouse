from django.db import models
from django.conf import settings

class Product(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')
    name = models.CharField(max_length=50, verbose_name='Название')
    indeficator = models.CharField(max_length=100, unique=True, verbose_name='Индефикатор товара')
    price_of_one = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Цена')
    count = models.PositiveIntegerField(default=0, verbose_name='Количество')
    manufacturer = models.CharField(max_length=100, verbose_name='Производитель')
    created_at = models.DateField(verbose_name='Дата изготовления')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='В продаже')
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Изображение', blank=True, null=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    @property
    def total_price(self):
        return self.price_of_one * self.count
