from django.contrib import admin
from django.urls import path
from .views import CreateCategory

app_name = "category"

urlpatterns = [
    path('create/', CreateCategory.as_view(), name="create_category"),
    path('admin/', admin.site.urls),
]