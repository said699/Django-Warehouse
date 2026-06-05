from django.urls import path, include
from . import views

app_name = 'organizations'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.seller_logout, name='logout'),
    path('profile/', views.profile, name='profile')
]