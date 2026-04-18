from django.db import models
from django import forms

class ManageBlog(forms.Form):
    name = forms.TextInput(required=True, verbose_name="Nombre del Blog")
    image = forms.ImageField(upload_to="", blank=True, null=True, verbose_name="Imagen del Blog")
    description = forms.Textarea(required=True, verbose_name="Descripcion del Blog")
    created_at = forms.DateField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return f"Nuevo Blog creado"