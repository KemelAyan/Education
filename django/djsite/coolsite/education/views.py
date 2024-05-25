from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name',max_length=100)

def index(request):
    return render(request, 'education/index.html',{"form":NameForm()})


def zayavka(request):
    return render(request, 'education/ru.html')

def zayavkaKz(request):
    return render(request, 'education/zayavkaKz.html')

def zayavkaRu(request):
    return render(request, 'education/zayavkaRu.html')
