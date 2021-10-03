from django import forms

from .models import MyHash

class MyHashForm(forms.ModelForm):
    
    class Meta:
        model=MyHash
        fields=('message',)