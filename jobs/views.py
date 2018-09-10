from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("L'amour n'est pas dans le pré, il est dans le lointain - Site en construction")
