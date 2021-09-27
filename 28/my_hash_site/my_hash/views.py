from django.shortcuts import render, redirect
from .models import MyHash
from .forms import MyHashForm
import hashlib

def my_hash_list(request):
    hashes = MyHash.objects.all().order_by('message')
    return render(request, 'my_hash/my_hash_list.html', {'hashes':hashes})

def my_hash_new(request):
    if request.method == "POST":
        form = MyHashForm(request.POST)
        if form.is_valid():
            my_hash = form.save(commit=False)
            msg = my_hash.message
            my_hash.my_hash = hashlib.sha256(msg.encode()).hexdigest() 
            my_hash.save()
            return redirect('/', pk=my_hash.pk)
    else:
        form = MyHashForm()
    return render(request, 'my_hash/edit.html', {'form': form})