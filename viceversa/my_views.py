from django.http import HttpResponse
from django.shortcuts import render

def houm(request):
    return render(request, 'home.html')