from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Blog


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
    fields = ["name", "preview", "category", "content"]
    template_name = "blog/create_blog.html"
    success_url = reverse_lazy("home")


# Delete a Blog by Site
class DeleteBlog(DeleteView):
    model = Blog
    template_name = "blog/delete_blog.html"
    success_url = reverse_lazy("home")


# Filter Blog by Category
def filter_blog(request, category):
    blog = Blog.objects.filter(category__name_category=category)

    if blog.exists():
        blog_data = list(blog.values("name", "preview", "category", "content", "created_at"))
        return JsonResponse({"blogs": blog_data})
    else:
        return JsonResponse({"blogs": [], "mensaje": "No hay blogs en esta categoria"})

    return render(request, "home/layout.html")