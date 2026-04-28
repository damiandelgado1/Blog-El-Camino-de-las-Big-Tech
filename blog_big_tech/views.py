from django.shortcuts import render
from blog.forms import SuscribeForm
from blog.models import Blog
from django.contrib import messages


# Display content of the Blog
def main_page(request):
    form = SuscribeForm()
    blogs = Blog.objects.all()
    return render(request, "home/home.html", {"form": form, "blogs": blogs})


# Filter content by Category
def filter_category(request, category):
    blogs = Blog.objects.filter(category=category)
    category = Blog.objects.all()

    return render(request,"blog/list_blog.html", {"blogs": blogs, "categorias": category})


# Form suscribe for receive new content
def form_suscribe(request):
    if request.method == "POST":
        form = SuscribeForm()

        if form.is_valid():
            name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]

            if "@gmail.com" not in email:
                messages.error(request, 'El email no tiene el "@gmail.com", debes Ingresarlo')

            else:
                messages.success(request, "La Suscripcion al Blog se realizo")
                form.save()

    else:
        form = SuscribeForm()

    return render(request, "home/form.html", {"form": form})