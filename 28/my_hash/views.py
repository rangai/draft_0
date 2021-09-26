from django.shortcuts import render

def my_hash_list(request):
    return render(request, 'my_hash/my_hash_list.html', {})