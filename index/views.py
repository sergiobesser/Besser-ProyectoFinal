from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html', {})

def about(request):
    return render(request, 'index/about.html', {})