from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    context = {
        
    }
    return render(request, 'projects.html', context)

def project_details(request):
    context = {
        
    }
    return render(request, 'project-details.html', context)

def services(request):
    return render(request, 'services.html')