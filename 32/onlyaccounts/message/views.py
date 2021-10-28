from django.shortcuts import render
from django.contrib.auth.models import User

def top(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "message/top.html", context)