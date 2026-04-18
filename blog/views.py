from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog


# Display Blog's
class ListBlog(ListView):
    model = Blog
    template_name = ""
    context_object_name = "Blogs"


# Detail a Blog in the Site
class DetailBlog(DetailView):
    model = Blog
    template_name = ""
    context_object_name = "Blog"


# Create a New Blog
@method_decorator(login_required, name="dispatch")
class CreateBlog(CreateView):
    model = Blog
    fields = ("name", "image", "description", "created_at")
    template_name = ""
    success_url = reverse_lazy("")


# Modify content a Blog
@method_decorator(login_required, name="dispatch")
class ModifyBlog(UpdateView):
    model = Blog
    fields = ("name", "image", "description")
    template_name = ""
    success_url = reverse_lazy("")


# Delete a Blog by Site
@method_decorator(login_required, name="dispatch")
class DeleteBlog(DeleteView):
    model = Blog
    template_name = ""
    success_url = reverse_lazy("")