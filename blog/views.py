from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class bloglistview(ListView):
    model=Post
    template_name='home.html'


class detailblogview(DetailView):
    model=Post
    template_name='post_detail.html'

class blogcreateview(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']

class blogupdateview(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']


class blogdeleteview(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url= reverse_lazy('home')