from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages

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