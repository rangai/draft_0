from django.urls import path
from django.urls.resolvers import URLPattern

from .views import index_view, room_view

app_name='chat'
urlpatterns = [
    path('', index_view, name='index'),
    path('room/<str:pk>', room_view, name='room'),
]