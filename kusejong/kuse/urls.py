from django.contrib import admin
from django.urls import path, include
from kuse import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('project/', views.projectView, name='project'),
    path('history/', views.historyView, name='history'),
    path('members/', views.membersView, name='members'),
    path('contact/', views.contactView, name='contact'),
]
