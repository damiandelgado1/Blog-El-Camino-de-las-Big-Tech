from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Blog
from django.contrib import messages


# Display Blog's
class ListBlog(ListView):
    model = Blog
    template_name = "blog/list_blog.html"
    context_object_name = "blogs"


# Detail a Blog in the Site
class DetailBlog(DetailView):
    model = Blog
    template_name = "blog/detail_blog.html"
    context_object_name = "blog"


# Create a New Blog
class CreateBlog(CreateView):
    model = Blog
    fields = ["name", "image", "category", "content"]
    template_name = "blog/create_blog.html"
    success_url = reverse_lazy("blog:blog_list")


# Delete a Blog by Site
class DeleteBlog(DeleteView):
    model = Blog
    template_name = "blog/delete_blog.html"
    success_url = reverse_lazy("home")