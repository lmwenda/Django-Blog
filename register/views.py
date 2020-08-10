from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def register(response):
    return render(response, "register/register.html", {})