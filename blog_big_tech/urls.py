from django.contrib import admin
from django.urls import path, include
from .views import main_page, form_suscribe

urlpatterns = [
    path('', main_page, name="home"),
    path('form/', form_suscribe, name="form"),
    path('blog/', include('blog.urls', namespace="blog")),
    path('admin/', admin.site.urls),
]