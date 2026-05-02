from django.contrib import admin
from category.models import Category

# Admin panel
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name_category"]
    list_filter = ["name_category"]
    search_fields = ["name_category"]