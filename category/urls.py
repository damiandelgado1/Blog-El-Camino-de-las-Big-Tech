from django.contrib import admin
from django.urls import path
from .views import ListCategory, CreateCategory


app_name = "category"

urlpatterns = [
    path('list/', ListCategory.as_view(), name="list_category"),
    path('create/', CreateCategory.as_view(), name="create_category"),
    path('admin/', admin.site.urls),
]