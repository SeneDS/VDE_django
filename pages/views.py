from django.shortcuts import render
from django.http import HttpResponse


def heme_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>hello world</h1>")

def about_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>About</h1>")

def contact_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>Contact</h1>")

# Create your views here.
