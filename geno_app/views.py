from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, "../templates/geno_app/application/home.html")

def database_description(request):
    return render(request, "../templates/geno_app/application/database_description.html", locals())