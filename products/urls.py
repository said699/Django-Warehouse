from django.urls import path, include
from . import views

app_name = 'products'

urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('products-list/', views.products_list, name='products_list'),
    path('<int:pk>/', views.product_info, name='product_info'),
    path('exit-prod/', views.exit_product, name='exit_product')
]