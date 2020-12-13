from frontend.models import Project
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ContactForm
from blog.models import Category, Post
from django.contrib import messages

def home(request):
    posts = Post.objects.all()[:4]
    context = {
        'posts':posts
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    paginator = Paginator(projects, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context={
        'page_obj': page_obj
    }
    return render(request, 'projects.html', context)

def project_details(request, id):
    projects = Project.objects.all()[:4]
    project = get_object_or_404(Project, pk=id)
    category = Category.objects.filter(project=project)
    context = {
        'project':project,
        'projects':projects,
        'category':category
    }
    return render(request, 'project-details.html', context)

def services(request):
    return render(request, 'services.html')

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            messages.success(request, "Thank you for contacting us, your message has been submitted.")
            return redirect('home')
        

    context = {
        'form' : form,
    }
    return render(request, 'contact.html', context)