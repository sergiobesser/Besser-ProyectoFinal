from django.shortcuts import render
from .models import Pages
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def pages(request):
    return render(request, 'pages/pages.html', {})


class List(ListView):
    model = Pages
    template_name = 'pages/pages_list.html'


class Detail(DetailView):
    model = Pages
    template_name = 'pages/pages_detail.html'


class New(LoginRequiredMixin, CreateView):
    model = Pages
    success_url = '/pages/list/'  
    fields = ['title', 'subtitle', 'body', 'image', 'author']


class Edit(LoginRequiredMixin, UpdateView):
    model = Pages
    success_url = '/pages/list/'  
    fields = ['title', 'subtitle', 'body', 'image', 'author']


class Delete(LoginRequiredMixin, DeleteView):
    model = Pages
    success_url = '/pages/list/'