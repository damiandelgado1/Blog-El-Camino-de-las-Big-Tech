from django.shortcuts import render
from .models import Category
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView


# Display all Categories in the Blog
class ListCategory(ListView):
    model = Category
    template_name = "category/list_category.html"
    context_object_name = "categories"

# Create a Category
class CreateCategory(CreateView):
    model = Category
    fields = ["name_category"]
    template_name = "category/create_category.html"
    success_url = reverse_lazy("home")