from django.contrib import admin
from .models import Van

@admin.register(Van)
class VanAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'status', 'is_featured']
    list_filter = ['category', 'status', 'charging_type', 'is_featured']
    search_fields = ['name', 'tagline']
    list_editable = ['is_featured']