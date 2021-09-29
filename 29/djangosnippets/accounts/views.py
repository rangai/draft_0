from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})