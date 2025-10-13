# ============================================================================
# FILE: vans/admin.py
# UPDATE: Use custom form and update image preview
# ============================================================================

from django.contrib import admin
from django.utils.html import format_html
from .models import Van
from .forms import VanAdminForm  # Add this import

@admin.register(Van)
class VanAdmin(admin.ModelAdmin):
    form = VanAdminForm  # Add this line
    
    list_display = [
        'id', 'image_preview', 'name', 'category', 'colored_badge', 
        'price_display', 'range_display', 'is_featured'
    ]
    
    list_filter = [
        'category', 'status', 'charging_type', 
        'is_featured', 'created_at'
    ]
    
    search_fields = ['name', 'tagline']
    list_editable = ['is_featured']
    ordering = ['created_at']
    list_per_page = 20
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'category', 'tagline', 'images')
        }),
        ('Status & Badge', {
            'fields': ('status', 'badge', 'badge_color')
        }),
        ('Specifications', {
            'fields': (
                'charging_type', 'range_km', 'power_kw', 
                'battery_capacity_kwh', 'payload_ton'
            )
        }),
        ('Pricing', {
            'fields': ('price', 'currency')
        }),
        ('Features', {
            'fields': ('is_featured', 'is_wishlisted')
        }),
    )
    
    @admin.display(description='Image')
    def image_preview(self, obj):
        if obj.images and len(obj.images) > 0:
            # Display Cloudinary image (first image)
            CLOUDINARY_BASE_URL = 'https://res.cloudinary.com/dak7ws0xx/image/upload/v1760352909'
            return format_html(
                '<img src="{}" class="van-image-thumb" />',
                f"{CLOUDINARY_BASE_URL}/{obj.images[0]}"
            )
        return '-'
    
    @admin.display(description='Badge')
    def colored_badge(self, obj):
        colors = {
            'green': '#10b981',
            'red': '#ef4444',
            'blue': '#3b82f6',
            'yellow': '#f59e0b'
        }
        color = colors.get(obj.badge_color, '#6b7280')
        return format_html(
            '<span style="background: {}; color: white; padding: 4px 12px; '
            'border-radius: 12px; font-size: 12px;">{}</span>',
            color, obj.badge
        )
    
    @admin.display(description='Price', ordering='price')
    def price_display(self, obj):
        return f"{obj.currency}{obj.price:,}"
    
    @admin.display(description='Range', ordering='range_km')
    def range_display(self, obj):
        return f"{obj.range_km} km"
    
    actions = ['mark_as_featured', 'mark_as_not_featured', 'mark_as_available']
    
    @admin.action(description='Mark selected as featured')
    def mark_as_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} van(s) marked as featured.')
    
    @admin.action(description='Remove featured status')
    def mark_as_not_featured(self, request, queryset):
        updated = queryset.update(is_featured=False)
        self.message_user(request, f'{updated} van(s) removed from featured.')
    
    @admin.action(description='Mark as available')
    def mark_as_available(self, request, queryset):
        updated = queryset.update(status='available')
        self.message_user(request, f'{updated} van(s) marked as available.')