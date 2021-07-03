from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from  django.urls import reverse_lazy

from .models import Post
class BListView(ListView):
    model = Post
    template_name='home.html'
class BDetailView(DetailView):
    model = Post
    template_name='post_detail.html'
class  BCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields='__all__'
class  BUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']
class BDeleteView(DeleteView):
    model=Post
    success_url=reverse_lazy('home')
    template_name='post_delete.html'
class First(ListView):
    model=Post
    template_name='first.html'

