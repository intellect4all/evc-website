from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project-details/', views.project_details, name='project-details'),
    path('services/', views.services, name='services'),
]