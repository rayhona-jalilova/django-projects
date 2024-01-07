from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView

from .models import Blog
# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Blog
    template_name = 'post_new.html'
    fields = ['title', 'author', 'description']

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'post_edit.html'
    fields = ['title', 'description']

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')