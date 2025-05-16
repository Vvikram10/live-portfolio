from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Experience, Certification, SocialLink
from .forms import ContactForm

def home_view(request):
    profile = Profile.objects.first()
    social_links = SocialLink.objects.all()
    return render(request, 'main/home.html', {
        'profile': profile,
        'social_links': social_links
    })

def about_view(request):
    profile = Profile.objects.first()
    return render(request, 'main/about.html', {
        'profile': profile
    })


def skills_view(request):
    # Get all skills
    skills = Skill.objects.all()  # Fetch all Skill objects from the database
    return render(request, 'main/skills.html', {'skills': skills})

def experience_view(request):
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'main/experience.html', {
        'experiences': experiences
    })

def certifications_view(request):
    certifications = Certification.objects.all().order_by('-date_obtained')
    return render(request, 'main/certifications.html', {
        'certifications': certifications
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    profile = Profile.objects.first()
    social_links = SocialLink.objects.all()
    
    return render(request, 'main/contact.html', {
        'form': form,
        'profile': profile,
        'social_links': social_links
    })