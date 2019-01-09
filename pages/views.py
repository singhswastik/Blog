# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class Bloglistview(ListView):
    model = Post
    template_name = 'home.html'

class Blogdetailview(DetailView):
    model = Post
    template_name = 'post_detail.html'

class Blogcreateview(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class Blogupdateview(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class Blogdeleteview(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class Aboutpageview(TemplateView):
    template_name = 'about.html'

class Servicespageview(TemplateView):
    template_name = 'Services.html'

class Categorypageview(TemplateView):
    template_name = 'Category.html'

class Contactpageview(TemplateView):
    template_name = 'Contact_us.html'


