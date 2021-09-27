from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_hash_list, name='my_hash_list'),
    path('my_hash/new/', views.my_hash_new, name='my_hash_new'),
]