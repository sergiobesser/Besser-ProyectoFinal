from django.shortcuts import render
from .models import Page
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView


def pages(request):
    return render(request, 'pages/pages.html', {})


class List(ListView):
    model = Page
    template_name = 'pages/pages_list.html'


class Detail(DetailView):
    model = Page
    template_name = 'pages/pages_detail.html'


class Edit(UpdateView):
    model = Page
    success_url = 'pages/pages_list.html'  
    fields = 'title', 'subtitle', 'body', 'author', 'image'


class Delete(DeleteView):
    model = Page
    success_url = 'pages/pages_list.html'