# ============================================================================
# FILE: blogs/serializers.py
# ============================================================================
"""
DRF serializers for blog API endpoints.
"""
from rest_framework import serializers
from .models import BlogPost


class BlogPostListSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for blog list views.
    Returns minimal fields for performance.
    """
    category_name = serializers.CharField(source='get_category_display_name', read_only=True)
    tag_list = serializers.ListField(source='get_tag_list', read_only=True)
    featured_image_url = serializers.SerializerMethodField()
    excerpt = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'slug',
            'meta_description',
            'excerpt',
            'author',
            'category',
            'category_name',
            'tag_list',
            'featured_image_url',
            'featured_image_alt',
            'is_featured',
            'reading_time',
            'views_count',
            'published_at',
            'created_at',
        ]
    
    def get_featured_image_url(self, obj):
        """Return full URL for featured image."""
        if obj.featured_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.featured_image.url)
            return obj.featured_image.url
        return None
    
    def get_excerpt(self, obj):
        """
        Generate excerpt from meta_description or first paragraph.
        """
        if obj.meta_description:
            return obj.meta_description
        
        # Extract first paragraph from content
        if obj.content and isinstance(obj.content, dict):
            blocks = obj.content.get('blocks', [])
            for block in blocks:
                if block.get('type') == 'paragraph':
                    text = block.get('data', {}).get('text', '')
                    # Remove HTML tags
                    import re
                    text = re.sub(r'<[^>]+>', '', text)
                    return text[:200] + '...' if len(text) > 200 else text
        
        return ''


class BlogPostDetailSerializer(serializers.ModelSerializer):
    """
    Full serializer for blog detail views.
    Returns all fields including full content.
    """
    category_name = serializers.CharField(source='get_category_display_name', read_only=True)
    tag_list = serializers.ListField(source='get_tag_list', read_only=True)
    featured_image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = [
            'id',
            'title',
            'slug',
            'meta_description',
            'author',
            'category',
            'category_name',
            'tags',
            'tag_list',
            'content',  # Full EditorJS content
            'featured_image_url',
            'featured_image_alt',
            'featured_image_caption',
            'status',
            'is_featured',
            'reading_time',
            'views_count',
            'published_at',
            'created_at',
            'updated_at',
        ]
    
    def get_featured_image_url(self, obj):
        """Return full URL for featured image."""
        if obj.featured_image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.featured_image.url)
            return obj.featured_image.url
        return None


class BlogPostWriteSerializer(serializers.ModelSerializer):
    """
    Serializer for creating/updating blog posts.
    """
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'slug',
            'meta_description',
            'author',
            'category',
            'tags',
            'content',
            'featured_image',
            'featured_image_alt',
            'featured_image_caption',
            'status',
            'is_featured',
        ]
        extra_kwargs = {
            'slug': {'required': False},  # Auto-generated if not provided
        }
    
    def validate_slug(self, value):
        """Ensure slug is unique."""
        instance = self.instance
        if instance:
            # Update: exclude current instance
            if BlogPost.objects.filter(slug=value).exclude(pk=instance.pk).exists():
                raise serializers.ValidationError("A blog post with this slug already exists.")
        else:
            # Create: check uniqueness
            if BlogPost.objects.filter(slug=value).exists():
                raise serializers.ValidationError("A blog post with this slug already exists.")
        return value