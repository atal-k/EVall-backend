# ============================================================================
# FILE: blogs/admin.py
# ============================================================================
"""
Enhanced Django admin for blog management with EditorJS integration.
"""
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.db.models import Q
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """
    Comprehensive admin interface for blog posts with rich features:
    - EditorJS integration for content editing
    - Auto-slug generation
    - Bulk actions for publishing/unpublishing
    - Advanced filtering and search
    - Image preview
    """
    
    # ========== List Display ==========
    list_display = [
        'title_with_status',
        'category_badge',
        'author',
        'featured_badge',
        'reading_time_display',
        'views_count',
        'published_date',
        'status_badge',
    ]
    
    list_display_links = ['title_with_status']
    
    # ========== Filters & Search ==========
    list_filter = [
        'status',
        'category',
        'is_featured',
        'created_at',
        'published_at',
    ]
    
    search_fields = [
        'title',
        'meta_description',
        'author',
        'tags',
    ]
    
    # ========== List Settings ==========
    list_per_page = 25
    list_max_show_all = 100
    date_hierarchy = 'published_at'
    
    # ========== Form Settings ==========
    fieldsets = (
        ('📝 Basic Information', {
            'fields': ('title', 'slug', 'author', 'meta_description')
        }),
        ('📚 Content', {
            'fields': ('content',),
            'description': 'Use the editor below to create rich, structured content with images, headings, lists, and more.'
        }),
        ('🖼️ Featured Image', {
            'fields': ('featured_image', 'featured_image_alt', 'featured_image_caption'),
            'classes': ('collapse',),
        }),
        ('🏷️ Categorization', {
            'fields': ('category', 'tags'),
        }),
        ('🚀 Publishing', {
            'fields': ('status', 'is_featured', 'published_at'),
            'description': 'Control publication status and visibility.'
        }),
        ('📊 Statistics', {
            'fields': ('reading_time', 'views_count', 'created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    
    readonly_fields = ['reading_time', 'views_count', 'created_at', 'updated_at']
    
    # Auto-populate slug from title
    prepopulated_fields = {'slug': ('title',)}
    
    # ========== Custom Display Methods ==========
    
    @admin.display(description='Title', ordering='title')
    def title_with_status(self, obj):
        """Display title with icon based on status."""
        icon = '📝' if obj.status == 'draft' else '✅'
        return format_html(
            '<strong>{} {}</strong>',
            icon,
            obj.title[:60] + '...' if len(obj.title) > 60 else obj.title
        )
    
    @admin.display(description='Category', ordering='category')
    def category_badge(self, obj):
        """Display category as colored badge."""
        colors = {
            'electronic-vehicles': '#10b981',
            'technological-advancements': '#3b82f6',
            'events': '#f59e0b',
            'news': '#ef4444',
            'reviews': '#8b5cf6',
            'services': '#06b6d4',
        }
        color = colors.get(obj.category, '#6b7280')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 10px; '
            'border-radius: 12px; font-size: 11px; font-weight: 600;">{}</span>',
            color,
            obj.get_category_display_name()
        )
    
    @admin.display(description='Featured', boolean=True, ordering='is_featured')
    def featured_badge(self, obj):
        """Display featured status."""
        return obj.is_featured
    
    @admin.display(description='Status', ordering='status')
    def status_badge(self, obj):
        """Display status as colored badge."""
        if obj.status == 'published':
            color = '#10b981'
            text = '● Published'
        else:
            color = '#f59e0b'
            text = '● Draft'
        
        return format_html(
            '<span style="color: {}; font-weight: 600;">{}</span>',
            color,
            text
        )
    
    @admin.display(description='Reading Time', ordering='reading_time')
    def reading_time_display(self, obj):
        """Display reading time with icon."""
        return format_html('📖 {} min', obj.reading_time)
    
    @admin.display(description='Published', ordering='published_at')
    def published_date(self, obj):
        """Display published date or 'Not published'."""
        if obj.published_at:
            return obj.published_at.strftime('%b %d, %Y')
        return format_html('<span style="color: #9ca3af;">Not published</span>')
    
    # ========== Bulk Actions ==========
    
    actions = [
        'publish_posts',
        'unpublish_posts',
        'mark_as_featured',
        'unmark_as_featured',
    ]
    
    @admin.action(description='✅ Publish selected posts')
    def publish_posts(self, request, queryset):
        """Bulk action to publish selected posts."""
        updated = 0
        for post in queryset.filter(status='draft'):
            post.status = 'published'
            if not post.published_at:
                post.published_at = timezone.now()
            post.save()
            updated += 1
        
        self.message_user(
            request,
            f'{updated} post(s) successfully published.'
        )
    
    @admin.action(description='📝 Unpublish selected posts')
    def unpublish_posts(self, request, queryset):
        """Bulk action to unpublish selected posts."""
        updated = queryset.filter(status='published').update(status='draft')
        self.message_user(
            request,
            f'{updated} post(s) moved to draft.'
        )
    
    @admin.action(description='⭐ Mark as featured')
    def mark_as_featured(self, request, queryset):
        """Bulk action to mark posts as featured."""
        updated = queryset.update(is_featured=True)
        self.message_user(
            request,
            f'{updated} post(s) marked as featured.'
        )
    
    @admin.action(description='⚪ Unmark as featured')
    def unmark_as_featured(self, request, queryset):
        """Bulk action to unmark posts as featured."""
        updated = queryset.update(is_featured=False)
        self.message_user(
            request,
            f'{updated} post(s) unmarked as featured.'
        )
    
    # ========== Custom Methods ==========
    
    def get_queryset(self, request):
        """Optimize queryset with select_related."""
        qs = super().get_queryset(request)
        return qs
    
    class Media:
        css = {
            'all': ('admin/css/custom_blog_admin.css',)
        }