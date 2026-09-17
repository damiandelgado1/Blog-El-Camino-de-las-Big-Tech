from django.contrib import admin
from blog.models import Blog


# Admin panel
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "content", "created_at"]
    list_filter = ["name", "category", "created_at"]
    search_fields = ["name", "category"]