from django.shortcuts import render, redirect


# Create your views here.

def homeView(request):
    return render(request, 'home.html') #home으로 변경할 것

def projectView(request):
    return render(request, 'project.html')

def historyView(request):
    return render(request, 'history.html')

def membersView(request):
    return render(request, 'members.html')

def contactView(request):
    return render(request, 'contact.html')