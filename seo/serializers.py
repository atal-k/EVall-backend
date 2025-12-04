# ============================================================================
# FILE: seo/serializers.py
# ============================================================================
"""
DRF serializers for SEO Tags API.
"""
from rest_framework import serializers
from django.utils import timezone
import pytz
from .models import SEOTag, AdvancedSEO


class TimezoneSerializerMixin:
    """Mixin to convert UTC datetime to Asia/Kolkata timezone."""
    
    def to_representation(self, instance):
        """Convert datetime fields to IST timezone."""
        representation = super().to_representation(instance)
        
        # Define IST timezone
        ist = pytz.timezone('Asia/Kolkata')
        
        # Convert datetime fields
        datetime_fields = ['created_at', 'updated_at']
        for field in datetime_fields:
            if field in representation and representation[field]:
                # Parse the datetime and convert to IST
                utc_dt = instance.created_at if field == 'created_at' else instance.updated_at
                if utc_dt:
                    ist_dt = utc_dt.astimezone(ist)
                    representation[field] = ist_dt.isoformat()
        
        return representation


class SEOTagSerializer(TimezoneSerializerMixin, serializers.ModelSerializer):
    """
    Full serializer for SEO tags (read operations).
    Returns all SEO fields for complete meta tag generation.
    """
    
    class Meta:
        model = SEOTag
        fields = [
            'id',
            'page_id',
            'page_path',
            'page_name',
            # Basic SEO
            'page_title',
            'meta_description',
            'meta_keywords',
            'canonical_url',
            'robots_meta',
            # Open Graph
            'og_title',
            'og_description',
            'og_type',
            'og_url',
            'og_image_url',
            'og_image_alt',
            # Twitter
            'twitter_card',
            'twitter_title',
            'twitter_description',
            'twitter_image_url',
            # Advanced
            'schema',
            # Metadata
            'created_at',
            'updated_at',
        ]


class SEOTagWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for creating/updating SEO tags.
    """
    
    class Meta:
        model = SEOTag
        fields = [
            'page_id',
            'page_path',
            'page_name',
            'page_title',
            'meta_description',
            'meta_keywords',
            'canonical_url',
            'robots_meta',
            'og_title',
            'og_description',
            'og_type',
            'og_url',
            'og_image_url',
            'og_image_alt',
            'twitter_card',
            'twitter_title',
            'twitter_description',
            'twitter_image_url',
            'schema',
        ]
    
    def validate_page_id(self, value):
        """Ensure page_id is unique on create."""
        instance = self.instance
        if instance:
            # Update: exclude current instance
            if SEOTag.objects.filter(page_id=value).exclude(pk=instance.pk).exists():
                raise serializers.ValidationError("A page with this ID already exists.")
        else:
            # Create: check uniqueness
            if SEOTag.objects.filter(page_id=value).exists():
                raise serializers.ValidationError("A page with this ID already exists.")
        return value
    
    def validate_page_title(self, value):
        """Validate page title length."""
        if len(value) > 70:
            raise serializers.ValidationError(
                f"Page title should be 70 characters or less (currently {len(value)})."
            )
        return value
    
    def validate_meta_description(self, value):
        """Validate meta description length."""
        if len(value) > 160:
            raise serializers.ValidationError(
                f"Meta description should be 160 characters or less (currently {len(value)})."
            )
        return value


class AdvancedSEOSerializer(TimezoneSerializerMixin, serializers.ModelSerializer):
    """
    Serializer for site-wide Advanced SEO settings.
    """
    
    class Meta:
        model = AdvancedSEO
        fields = [
            'id',
            'google_site_verification',
            'header_script',
            'footer_script',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class FullSEOSerializer(serializers.Serializer):
    """
    Combined serializer for full SEO data.
    Returns all page SEO tags + site-wide advanced SEO.
    """
    
    seo_tags = SEOTagSerializer(many=True)
    advanced_seo = AdvancedSEOSerializer()
