from django.db import models
from django import forms

class SuscribeForm(forms.Form):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=20, required=True)