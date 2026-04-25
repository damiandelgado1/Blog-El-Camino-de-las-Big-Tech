from django.shortcuts import render
from blog.forms import SuscribeForm
from blog.models import Blog

def main_page(request):
    form = SuscribeForm()
    blogs = Blog.objects.all()
    return render(request, "home/home.html", {"form": form, "blog": blogs})