from django.shortcuts import render
from .models import Category
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create a Category
class CreateCategory(CreateView):
    model = Category
    fields = ["name_category"]
    template_name = "category/create_category.html"
    success_url = reverse_lazy("home")