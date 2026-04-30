from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

CURRENCY_CHOICES = [
    ('USD', '$'),
    ('RUB', '₽'),
    ('UZS', 'so`m')
]

class Organization(AbstractUser):
    name = models.CharField(max_length=90, verbose_name='Название вашей организации')
    inn = models.CharField(max_length=12, unique=True, verbose_name='ИНН')
    phone = PhoneNumberField(region="RU", verbose_name='Номер телефона')
    website = models.URLField(blank=True, verbose_name='Сайт организации')
    logo = models.ImageField(upload_to='organizations_logo/%Y/%m/%d', verbose_name='Логотип', blank=True, null=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, verbose_name='Валюта учёта')
    address = models.TextField(verbose_name='Адрес склада')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
