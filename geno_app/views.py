from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, "../templates/geno_app/application/home.html")

def database_description(request):
    return render(request, "../templates/geno_app/application/database_description.html", locals())

def search(request):
    return render(request, "../templates/geno_app/application/search.html", locals())

def analysis(request):
    return render(request, "../templates/geno_app/application/analysis.html", locals())

def online_tools(request):
    return render(request, "../templates/geno_app/application/online_tools.html", locals())
