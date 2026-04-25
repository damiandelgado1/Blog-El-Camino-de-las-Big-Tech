from django.contrib import admin
from django.urls import path
from .views import ListBlog, DetailBlog, CreateBlog, DeleteBlog

app_name = "blog"

urlpatterns = [
    path('list/', ListBlog.as_view(), name="blog_list"),
    path('detail/<int:pk>/', DetailBlog.as_view(), name="blog_detail"),
    path('create/', CreateBlog.as_view(), name="create_blog"),
    path('delete/<int:pk>/', DeleteBlog.as_view(), name="delete_blog"),
    path('admin/', admin.site.urls),
]