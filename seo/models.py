# ============================================================================
# FILE: seo/models.py
# ============================================================================
"""
SEO Tags model for managing meta tags across all pages.
Maps to Next.js page IDs from navMenuData for clean integration.
"""
from django.db import models
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class SEOTag(models.Model):
    """
    Centralized SEO meta tags for all website pages.
    Uses page_id as primary identifier matching frontend navMenuData.
    """
    
    OG_TYPE_CHOICES = [
        ('website', 'Website'),
        ('article', 'Article'),
        ('product', 'Product'),
    ]
    
    TWITTER_CARD_CHOICES = [
        ('summary', 'Summary'),
        ('summary_large_image', 'Summary Large Image'),
        ('app', 'App'),
        ('player', 'Player'),
    ]
    
    # ========== Primary Identifiers ==========
    page_id = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
        help_text="Unique page identifier from navMenuData (e.g., 'home', 'company-overview')"
    )
    
    page_path = models.CharField(
        max_length=255,
        db_index=True,
        help_text="URL path for this page (e.g., '/', '/what-drives-us/company-overview')"
    )
    
    page_name = models.CharField(
        max_length=150,
        help_text="Human-readable page name for admin reference"
    )
    
    # ========== Basic SEO ==========
    page_title = models.CharField(
        max_length=70,
        help_text="Browser tab title (recommended: 50-60 characters)"
    )
    
    meta_description = models.CharField(
        max_length=160,
        help_text="SEO meta description (recommended: 150-160 characters)"
    )
    
    meta_keywords = models.CharField(
        max_length=255,
        blank=True,
        help_text="Comma-separated keywords (e.g., 'electric vehicles, EV, commercial')"
    )
    
    canonical_url = models.URLField(
        max_length=500,
        blank=True,
        help_text="Canonical URL to prevent duplicate content issues"
    )
    
    robots_meta = models.CharField(
        max_length=100,
        default='index, follow',
        help_text="Robots meta tag (e.g., 'index, follow', 'noindex, nofollow')"
    )
    
    # ========== Open Graph (Facebook, LinkedIn) ==========
    og_title = models.CharField(
        max_length=95,
        help_text="Open Graph title (recommended: 60-90 characters)"
    )
    
    og_description = models.CharField(
        max_length=200,
        help_text="Open Graph description (recommended: 150-200 characters)"
    )
    
    og_type = models.CharField(
        max_length=20,
        choices=OG_TYPE_CHOICES,
        default='website',
        help_text="Open Graph content type"
    )
    
    og_url = models.URLField(
        max_length=500,
        help_text="Open Graph URL (full absolute URL)"
    )
    
    og_image_url = models.URLField(
        max_length=500,
        help_text="Open Graph image URL (recommended: 1200x630px, CDN hosted)"
    )
    
    og_image_alt = models.CharField(
        max_length=255,
        blank=True,
        help_text="Alt text for OG image (accessibility)"
    )
    
    # ========== Twitter Card ==========
    twitter_card = models.CharField(
        max_length=30,
        choices=TWITTER_CARD_CHOICES,
        default='summary_large_image',
        help_text="Twitter card type"
    )
    
    twitter_title = models.CharField(
        max_length=70,
        help_text="Twitter card title"
    )
    
    twitter_description = models.CharField(
        max_length=200,
        help_text="Twitter card description"
    )
    
    twitter_image_url = models.URLField(
        max_length=500,
        help_text="Twitter card image URL (recommended: 1200x628px, CDN hosted)"
    )
    
    # ========== Advanced SEO ==========
    schema = models.JSONField(
        blank=True,
        null=True,
        help_text="JSON-LD structured data for rich snippets"
    )
    
    # ========== Timestamps ==========
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=150, blank=True)
    updated_by = models.CharField(max_length=150, blank=True)
    
    class Meta:
        verbose_name = "SEO Tag"
        verbose_name_plural = "SEO Tags"
        ordering = ['page_id']
        indexes = [
            models.Index(fields=['page_id']),
            models.Index(fields=['page_path']),
        ]
    
    def __str__(self):
        return f"{self.page_name} ({self.page_id})"
    
    def clean(self):
        """Validate URL fields."""
        url_validator = URLValidator()
        
        # Validate image URLs
        if self.og_image_url:
            try:
                url_validator(self.og_image_url)
            except ValidationError:
                raise ValidationError({'og_image_url': 'Enter a valid URL.'})
        
        if self.twitter_image_url:
            try:
                url_validator(self.twitter_image_url)
            except ValidationError:
                raise ValidationError({'twitter_image_url': 'Enter a valid URL.'})
    
    def save(self, *args, **kwargs):
        """Auto-populate related fields if empty."""
        # Auto-populate OG fields from basic SEO if empty
        if not self.og_title:
            self.og_title = self.page_title
        if not self.og_description:
            self.og_description = self.meta_description
        if not self.og_url:
            self.og_url = f"https://www.evall.in{self.page_path}"
        
        # Auto-populate Twitter fields from OG if empty
        if not self.twitter_title:
            self.twitter_title = self.og_title
        if not self.twitter_description:
            self.twitter_description = self.og_description
        if not self.twitter_image_url:
            self.twitter_image_url = self.og_image_url
        
        super().save(*args, **kwargs)


class AdvancedSEO(models.Model):
    """
    Site-wide advanced SEO settings (Singleton model).
    Only one instance should exist for the entire site.
    """
    
    google_site_verification = models.TextField(
        blank=True,
        help_text='Google Site Verification meta tag content (e.g., <meta name="google-site-verification" content="your-code">)'
    )
    
    header_script = models.TextField(
        blank=True,
        help_text='Scripts to be added in <head> section (e.g., Google Analytics, Meta Pixel)'
    )
    
    footer_script = models.TextField(
        blank=True,
        help_text='Scripts to be added before </body> closing tag (e.g., Chat widgets, Additional tracking)'
    )
    
    # ========== Timestamps ==========
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=150, blank=True)
    updated_by = models.CharField(max_length=150, blank=True)
    
    class Meta:
        verbose_name = "Advanced SEO Setting"
        verbose_name_plural = "Advanced SEO Settings"
    
    def __str__(self):
        return "Advanced SEO Settings"
    
    def save(self, *args, **kwargs):
        """Ensure only one instance exists (singleton pattern)."""
        self.pk = 1
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        """Prevent deletion of the singleton instance."""
        pass
    
    @classmethod
    def load(cls):
        """Get or create the singleton instance."""
        obj, created = cls.objects.get_or_create(pk=1)
        return obj