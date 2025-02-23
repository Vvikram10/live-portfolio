from django.shortcuts import render
from django.http import JsonResponse
from .models import Certificate, Project, Skill, Contact

def home(request):
    skills = Skill.objects.all()
    return render(request, 'main_app/home.html', {'skills': skills})

def about(request):
    skills = Skill.objects.all()
    return render(request, 'main_app/about.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'main_app/projects.html', {'projects': projects})

def contact(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        return JsonResponse({'status': 'success'})
    return render(request, 'main_app/contact.html')

def certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'main_app/certificates.html', {
        'certificates': certificates
    })