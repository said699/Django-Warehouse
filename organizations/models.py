from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

class MySellerManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Email обязан быть!')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        
        if kwargs.get('is_staff') == False:
            raise ValueError("Супер юзер должен иметь is_staff=True")
        if kwargs.get('is_superuser') == False:
            raise ValueError('Супер юзер должен иметь is_superuser=True')

        return self.create_user(email=email, password=password, **kwargs)
        

class Seller(AbstractUser):
    username = None
    name = models.CharField(max_length=90, verbose_name='Ваше имя')
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email')
    phone = PhoneNumberField(unique=True, verbose_name='Номер телефона') 
    address = models.TextField(verbose_name='Адрес магазина, или склада, или Ваш')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Текущий счёт')
    
    objects = MySellerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return self.name
