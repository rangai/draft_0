from django.urls import path
from message import views

urlpatterns = [
    path("receive/", views.receive, name="receive"),
    path("send/", views.send, name="send"),
]