from django.shortcuts import render
from django.http import HttpResponse
from .models import job

#
def home(request):
    # return HttpResponse("L'amour n'est pas dans le pré, il est dans le lointain - Site en construction")
    jobs = job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})