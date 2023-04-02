from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),  
    path('base/', views.register, name='base'),
    path('login/', views.user_login, name='login'),     
]
