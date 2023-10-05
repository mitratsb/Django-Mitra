from django.shortcuts import render
from instagram.models import mypost

# Create your views here.


def h1(request):
    return render (request, 'instagram/h1.html', {})

def profile1(request):
    myposts= mypost.objects.all()
    return render (request, 'instagram/profile1.html', {"myposts":myposts})

def profile2(request):
    return render (request, 'instagram/profile2.html', {})
