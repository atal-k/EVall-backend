# ============================================================================
# FILE: blogs/views.py
# ============================================================================
"""
DRF ViewSets for blog API endpoints.
"""
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import BlogPost
from .serializers import (
    BlogPostListSerializer,
    BlogPostDetailSerializer,
    BlogPostWriteSerializer
)


class BlogPostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for blog post CRUD operations.
    
    Endpoints:
    - GET    /api/blogs/          - List all published blogs
    - POST   /api/blogs/          - Create new blog
    - GET    /api/blogs/{slug}/   - Get blog detail
    - PUT    /api/blogs/{slug}/   - Update blog
    - PATCH  /api/blogs/{slug}/   - Partial update
    - DELETE /api/blogs/{slug}/   - Delete blog
    
    Custom Actions:
    - POST /api/blogs/{slug}/publish/   - Publish a draft
    - POST /api/blogs/{slug}/unpublish/ - Unpublish a post
    - GET  /api/blogs/featured/         - Get featured posts
    - GET  /api/blogs/by_category/      - Get posts by category
    """
    
    queryset = BlogPost.objects.all()
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtering
    filterset_fields = ['status', 'category', 'is_featured', 'author']
    
    # Search
    search_fields = ['title', 'meta_description', 'tags', 'author']
    
    # Ordering
    ordering_fields = ['published_at', 'created_at', 'views_count', 'title']
    ordering = ['-published_at']
    
    def get_queryset(self):
        """
        By default, only return published posts.
        Include drafts if 'include_drafts=true' query param is set.
        """
        queryset = super().get_queryset()
        
        # By default, show only published posts
        include_drafts = self.request.query_params.get('include_drafts', 'false')
        if include_drafts.lower() != 'true':
            queryset = queryset.filter(status='published')
        
        return queryset
    
    def get_serializer_class(self):
        """
        Use different serializers for different actions.
        """
        if self.action in ['list', 'featured', 'by_category', 'latest']:
            return BlogPostListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return BlogPostWriteSerializer
        return BlogPostDetailSerializer
    
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a single blog post and increment view count.
        """
        instance = self.get_object()
        
        # Increment view count
        instance.increment_views()
        
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        """
        Get all featured blog posts.
        GET /api/blogs/featured/
        """
        featured_posts = self.get_queryset().filter(is_featured=True)
        
        page = self.paginate_queryset(featured_posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(featured_posts, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_category(self, request):
        """
        Get blog posts by category.
        GET /api/blogs/by_category/?category=news
        """
        category = request.query_params.get('category')
        
        if not category:
            return Response(
                {'error': 'Category parameter is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        posts = self.get_queryset().filter(category=category)
        
        page = self.paginate_queryset(posts)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def latest(self, request):
        """
        Get latest blog posts.
        GET /api/blogs/latest/?limit=5
        """
        limit = request.query_params.get('limit', 5)
        
        try:
            limit = int(limit)
            if limit <= 0:
                limit = 5
        except (ValueError, TypeError):
            limit = 5
        
        latest_posts = self.get_queryset().order_by('-published_at')
        
        # Manually paginate with limit
        paginated_posts = latest_posts[:limit]
        
        serializer = self.get_serializer(paginated_posts, many=True)
        
        return Response({
            'count': latest_posts.count(),
            'next': None,
            'previous': None,
            'results': serializer.data
        })
    
    @action(detail=True, methods=['post'])
    def publish(self, request, slug=None):
        """
        Publish a draft blog post.
        POST /api/blogs/{slug}/publish/
        """
        blog_post = self.get_object()
        
        if blog_post.status == 'published':
            return Response(
                {'message': 'Blog post is already published'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        blog_post.status = 'published'
        if not blog_post.published_at:
            blog_post.published_at = timezone.now()
        blog_post.save()
        
        serializer = self.get_serializer(blog_post)
        return Response({
            'message': 'Blog post published successfully',
            'data': serializer.data
        })
    
    @action(detail=True, methods=['post'])
    def unpublish(self, request, slug=None):
        """
        Unpublish a blog post (move to draft).
        POST /api/blogs/{slug}/unpublish/
        """
        blog_post = self.get_object()
        
        if blog_post.status == 'draft':
            return Response(
                {'message': 'Blog post is already a draft'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        blog_post.status = 'draft'
        blog_post.save()
        
        serializer = self.get_serializer(blog_post)
        return Response({
            'message': 'Blog post unpublished successfully',
            'data': serializer.data
        })