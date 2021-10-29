from django.shortcuts import render
from django.contrib.auth.models import User

def top(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "message/top.html", context)

def receive(request):
    return render(request, "message/receive.html")

def send(request):
    return render(request, "message/send.html")