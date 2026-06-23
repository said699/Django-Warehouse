from django.urls import path, include
from . import views

app_name = 'sellers'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.seller_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('del-acc/', views.delete_acc, name='delete_acc')
]