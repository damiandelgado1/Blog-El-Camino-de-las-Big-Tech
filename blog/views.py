from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Blog
from .forms import SuscribeForm
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
    fields = ("name", "image", "category", "content")
    template_name = "blog/create_blog.html"
    success_url = reverse_lazy("blog:blog_list")


# Delete a Blog by Site
class DeleteBlog(DeleteView):
    model = Blog
    template_name = "blog/delete_blog.html"
    success_url = reverse_lazy("home")

def form_suscribe(request):
    if request.method == "POST":
        form = SuscribeForm()

        if form.is_valid():
            name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]

            if "@gmail.com" not in email:
                messages.error(request, 'El email no tiene el "@gmail.com", debes ingresarlo para Completar el Registro')

            else:
                messages.success(request, "La suscripcion al Blog se ha hecho correctamente")
                form.save()

    else:
        form = SuscribeForm()

    return render(request, "home/form.html", {"form": form})