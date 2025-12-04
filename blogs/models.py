# ============================================================================
# FILE: blogs/models.py (FIXED)
# ============================================================================
"""
Blog models with EditorJS integration for rich content editing.
"""
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django_editorjs_fields import EditorJsJSONField, EditorJsTextField
import re


class BlogPost(models.Model):
    """
    Main blog post model with EditorJS structured content.
    Supports rich content blocks: headers, paragraphs, images, lists, quotes, etc.
    """
    
    # Predefined categories for Electric Vehicle blog
    CATEGORY_CHOICES = [
        ('electronic-vehicles', 'Electronic Vehicles'),
        ('technological-advancements', 'Technological Advancements'),
        ('events', 'Events'),
        ('news', 'News'),
        ('reviews', 'Reviews'),
        ('services', 'Services'),
    ]
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    # ========== Basic Information ==========
    title = models.CharField(
        max_length=255,
        db_index=True,
        help_text="Blog post title (max 255 characters)"
    )
    
    slug = models.SlugField(
        max_length=280,
        unique=True,
        db_index=True,
        help_text="URL-friendly version of title (auto-generated if left blank)"
    )
    
    meta_description = models.CharField(
        max_length=160,
        blank=True,
        help_text="SEO meta description (recommended 150-160 characters)"
    )
    
    # ========== Rich Content (EditorJS) ==========
    content = EditorJsJSONField(
        plugins=[
            "@editorjs/paragraph",
            "@editorjs/header",
            "@editorjs/list@latest",  # List plugin
            "@editorjs/image",
            "@editorjs/quote",
            "@editorjs/delimiter",
            "@editorjs/link",
            "editorjs-hyperlink",
            "@editorjs/raw",
            "@editorjs/checklist",
            "@editorjs/table",
        ],
        tools={
            # FIXED: Single, properly configured list tool
            # "List": {  # Match the case from your API responses
            #     "class": "List",
            #     "inlineToolbar": True,
            #     "config": {
            #         "defaultStyle": "unordered"
            #     }
            # },
            # Alternative approach - also keep lowercase for compatibility
            "list": {
                "class": "List",
                "inlineToolbar": True,
                "config": {
                    "defaultStyle": "unordered"
                }
            },
            "Image": {
                "config": {
                    "endpoints": {
                        "byFile": "/editorjs/image_upload/"
                    }
                }
            },
            "Hyperlink": {
                "class": "Hyperlink",
                "config": {
                    "shortcut": 'CMD+L',
                    "target": '_blank',
                    "rel": 'nofollow',
                    "availableTargets": ['_blank', '_self'],
                    "availableRels": ['author', 'noreferrer'],
                    "validate": False,
                }
            },
        },
        null=True,
        blank=True,
        help_text="Main blog content with rich formatting"
    )
    
    # ========== Featured Image ==========
    featured_image = models.ImageField(
        upload_to='blog_featured/%Y/%m/',
        blank=True,
        null=True,
        help_text="Featured image for blog preview/card (recommended: 1200x630px)"
    )
    
    featured_image_alt = models.CharField(
        max_length=255,
        blank=True,
        help_text="Alt text for featured image (SEO & accessibility)"
    )
    
    featured_image_caption = models.CharField(
        max_length=255,
        blank=True,
        help_text="Optional caption for featured image"
    )
    
    # ========== Author & Categorization ==========
    author = models.CharField(
        max_length=150,
        default="Admin",
        help_text="Author name"
    )
    
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='news',
        db_index=True,
        help_text="Select blog category"
    )
    
    tags = models.CharField(
        max_length=300,
        blank=True,
        help_text="Comma-separated tags (e.g., tesla, charging, battery)"
    )
    
    # ========== Status & Publishing ==========
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
        db_index=True,
        help_text="Publication status"
    )
    
    is_featured = models.BooleanField(
        default=False,
        db_index=True,
        help_text="Mark as featured to highlight on homepage"
    )
    
    # ========== Timestamps ==========
    published_at = models.DateTimeField(
        null=True,
        blank=True,
        db_index=True,
        help_text="Publication date/time (auto-set when published)"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # ========== Computed Fields ==========
    reading_time = models.IntegerField(
        default=0,
        help_text="Estimated reading time in minutes (auto-calculated)"
    )
    
    views_count = models.IntegerField(
        default=0,
        help_text="Number of times this post has been viewed"
    )
    
    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-published_at', '-created_at']
        indexes = [
            models.Index(fields=['-published_at']),
            models.Index(fields=['status', '-published_at']),
            models.Index(fields=['category', '-published_at']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """
        Override save to auto-generate slug and calculate reading time.
        """
        # Auto-generate slug from title if not provided
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure unique slug
            original_slug = self.slug
            counter = 1
            while BlogPost.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        
        # Set published_at timestamp when status changes to published
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        
        # Calculate reading time based on content
        self.reading_time = self.calculate_reading_time()
        
        super().save(*args, **kwargs)
    
    def calculate_reading_time(self):
        """
        Calculate estimated reading time based on word count.
        Average reading speed: 200 words per minute.
        """
        if not self.content:
            return 1
        
        word_count = 0
        
        # Extract text from EditorJS blocks
        if isinstance(self.content, dict) and 'blocks' in self.content:
            for block in self.content['blocks']:
                if block.get('type') in ['paragraph', 'header', 'quote', 'Header']:
                    text = block.get('data', {}).get('text', '')
                    # Remove HTML tags and count words
                    text = re.sub(r'<[^>]+>', '', text)
                    word_count += len(text.split())
                elif block.get('type') in ['list', 'List']:  # Handle both cases
                    items = block.get('data', {}).get('items', [])
                    for item in items:
                        text = re.sub(r'<[^>]+>', '', str(item))
                        word_count += len(text.split())
        
        # Calculate reading time (200 words per minute)
        reading_time = max(1, round(word_count / 200))
        return reading_time
    
    def get_category_display_name(self):
        """Get human-readable category name."""
        return dict(self.CATEGORY_CHOICES).get(self.category, self.category)
    
    def get_tag_list(self):
        """Return tags as a list."""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',') if tag.strip()]
        return []
    
    def increment_views(self):
        """Increment view count."""
        self.views_count += 1
        self.save(update_fields=['views_count'])