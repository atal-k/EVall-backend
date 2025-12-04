# ============================================================================
# FILE: seo/admin.py
# ============================================================================
"""
Enhanced Django admin for SEO tags management.
Features: Live preview, bulk actions, character count, validation.
"""
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
import pytz
from .models import SEOTag, AdvancedSEO


@admin.register(SEOTag)
class SEOTagAdmin(admin.ModelAdmin):
    """
    Comprehensive admin interface for SEO tag management.
    """
    
    # ========== List Display ==========
    list_display = [
        'page_id_display',
        'page_name_display',
        'page_path_short',
        'title_preview',
        'last_updated_ist',
    ]
    
    list_display_links = ['page_id_display']
    
    # ========== Filters & Search ==========
    list_filter = [
        'og_type',
        'twitter_card',
        'created_at',
        'updated_at',
    ]
    
    search_fields = [
        'page_id',
        'page_name',
        'page_path',
        'page_title',
        'meta_description',
        'meta_keywords',
    ]
    
    # ========== List Settings ==========
    list_per_page = 25
    date_hierarchy = 'updated_at'
    
    # ========== Form Settings ==========
    fieldsets = (
        ('🔑 Page Identification', {
            'fields': ('page_id', 'page_path', 'page_name'),
            'description': 'Primary identifiers - page_id must match navMenuData in frontend'
        }),
        ('📝 Basic SEO', {
            'fields': (
                'page_title',
                'meta_description',
                'meta_keywords',
                'canonical_url',
                'robots_meta',
            ),
            'description': 'Core SEO meta tags for search engines'
        }),
        ('📱 Open Graph (Facebook, LinkedIn)', {
            'fields': (
                'og_title',
                'og_description',
                'og_type',
                'og_url',
                'og_image_url',
                'og_image_alt',
            ),
            'classes': ('collapse',),
            'description': 'Meta tags for social media sharing'
        }),
        ('🐦 Twitter Card', {
            'fields': (
                'twitter_card',
                'twitter_title',
                'twitter_description',
                'twitter_image_url',
            ),
            'classes': ('collapse',),
            'description': 'Twitter-specific meta tags'
        }),
        ('⚙️ Advanced', {
            'fields': (
                'schema',
            ),
            'classes': ('collapse',),
            'description': 'JSON-LD structured data for rich snippets'
        }),
        ('📊 Metadata', {
            'fields': (
                'created_at_display',
                'updated_at_display',
                'created_by',
                'updated_by',
            ),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ['created_at_display', 'updated_at_display']
    
    # ========== Custom Display Methods ==========
    
    def get_ist_time(self, dt):
        """Convert UTC datetime to IST."""
        if dt:
            ist = pytz.timezone('Asia/Kolkata')
            return dt.astimezone(ist)
        return None
    
    @admin.display(description='Created At (IST)')
    def created_at_display(self, obj):
        """Display created time in IST."""
        ist_time = self.get_ist_time(obj.created_at)
        if ist_time:
            return ist_time.strftime('%b %d, %Y %I:%M:%S %p IST')
        return '-'
    
    @admin.display(description='Updated At (IST)')
    def updated_at_display(self, obj):
        """Display updated time in IST."""
        ist_time = self.get_ist_time(obj.updated_at)
        if ist_time:
            return ist_time.strftime('%b %d, %Y %I:%M:%S %p IST')
        return '-'
    
    @admin.display(description='Page ID', ordering='page_id')
    def page_id_display(self, obj):
        """Display page_id with icon."""
        return format_html(
            '<strong style="font-family: monospace; color: #0066cc;">📄 {}</strong>',
            obj.page_id
        )
    
    @admin.display(description='Page Name', ordering='page_name')
    def page_name_display(self, obj):
        """Display page name."""
        return format_html(
            '<span style="font-weight: 500;">{}</span>',
            obj.page_name
        )
    
    @admin.display(description='Path', ordering='page_path')
    def page_path_short(self, obj):
        """Display shortened path."""
        path = obj.page_path
        if len(path) > 40:
            path = path[:37] + '...'
        return format_html(
            '<code style="color: #666; font-size: 12px;">{}</code>',
            path
        )
    
    @admin.display(description='Title Preview')
    def title_preview(self, obj):
        """Display title with character count."""
        char_count = len(obj.page_title)
        color = '#10b981' if char_count <= 60 else '#f59e0b' if char_count <= 70 else '#ef4444'
        
        title = obj.page_title[:50] + '...' if len(obj.page_title) > 50 else obj.page_title
        
        return format_html(
            '{}<br><small style="color: {};">({} chars)</small>',
            title,
            color,
            char_count
        )
    
    @admin.display(description='Last Updated (IST)', ordering='updated_at')
    def last_updated_ist(self, obj):
        """Display last update time in IST."""
        ist_time = self.get_ist_time(obj.updated_at)
        if ist_time:
            return ist_time.strftime('%b %d, %Y %I:%M %p')
        return '-'
    
    # ========== Custom Methods ==========
    
    def save_model(self, request, obj, form, change):
        """Track who created/updated the record."""
        if not change:  # Creating new
            obj.created_by = request.user.username
        obj.updated_by = request.user.username
        super().save_model(request, obj, form, change)


@admin.register(AdvancedSEO)
class AdvancedSEOAdmin(admin.ModelAdmin):
    """
    Admin interface for site-wide Advanced SEO settings (singleton).
    """
    
    # ========== Form Settings ==========
    fieldsets = (
        ('🔍 Google Site Verification', {
            'fields': ('google_site_verification',),
            'description': 'Add Google Site Verification meta tag content'
        }),
        ('📜 Header Scripts', {
            'fields': ('header_script',),
            'description': 'Scripts to be added in <head> section (Analytics, Pixels, etc.)'
        }),
        ('📜 Footer Scripts', {
            'fields': ('footer_script',),
            'description': 'Scripts to be added before </body> tag (Chat widgets, etc.)'
        }),
        ('📊 Metadata', {
            'fields': (
                'created_at_display',
                'updated_at_display',
                'created_by',
                'updated_by',
            ),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ['created_at_display', 'updated_at_display']
    
    def get_ist_time(self, dt):
        """Convert UTC datetime to IST."""
        if dt:
            ist = pytz.timezone('Asia/Kolkata')
            return dt.astimezone(ist)
        return None
    
    @admin.display(description='Created At (IST)')
    def created_at_display(self, obj):
        """Display created time in IST."""
        ist_time = self.get_ist_time(obj.created_at)
        if ist_time:
            return ist_time.strftime('%b %d, %Y %I:%M:%S %p IST')
        return '-'
    
    @admin.display(description='Updated At (IST)')
    def updated_at_display(self, obj):
        """Display updated time in IST."""
        ist_time = self.get_ist_time(obj.updated_at)
        if ist_time:
            return ist_time.strftime('%b %d, %Y %I:%M:%S %p IST')
        return '-'
    
    def has_add_permission(self, request):
        """Restrict to single instance."""
        return not AdvancedSEO.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of singleton."""
        return False
    
    def save_model(self, request, obj, form, change):
        """Track who created/updated the record."""
        if not change:
            obj.created_by = request.user.username
        obj.updated_by = request.user.username
        super().save_model(request, obj, form, change)

