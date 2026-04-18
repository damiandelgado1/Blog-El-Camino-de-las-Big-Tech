from django.contrib import admin
from blog.models import Blog

# Admin panel
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at"]
    list_filter = ["name", "created_at"]
    search_fields = ["name"]