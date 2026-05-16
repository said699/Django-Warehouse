from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('list_products/', views.warehouse, name='warehouse'),
]