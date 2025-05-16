from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('skills/', views.skills_view, name='skills'),
    path('experience/', views.experience_view, name='experience'),
    path('certifications/', views.certifications_view, name='certifications'),
    path('contact/', views.contact_view, name='contact'),
]