# ============================================================================
# FILE: seo/views.py
# ============================================================================
"""
DRF ViewSets for SEO Tags API endpoints.
"""
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import SEOTag, AdvancedSEO
from .serializers import (
    SEOTagSerializer,
    SEOTagWriteSerializer,
    AdvancedSEOSerializer,
    FullSEOSerializer
)


class SEOTagViewSet(viewsets.ModelViewSet):
    """
    ViewSet for SEO tag CRUD operations.
    
    Endpoints:
    - GET    /api/seo/                 - List all SEO tags (all pages)
    - POST   /api/seo/                 - Create new SEO tag
    - GET    /api/seo/{page_id}/       - Get SEO by page_id
    - PUT    /api/seo/{page_id}/       - Update SEO tag
    - PATCH  /api/seo/{page_id}/       - Partial update
    - DELETE /api/seo/{page_id}/       - Delete SEO tag
    - GET    /api/seo/full-seo/        - Get all SEO tags + Advanced SEO
    """
    
    queryset = SEOTag.objects.all()
    lookup_field = 'page_id'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Filtering
    filterset_fields = ['og_type', 'twitter_card']
    
    # Search
    search_fields = ['page_id', 'page_name', 'page_path', 'page_title', 'meta_keywords']
    
    # Ordering
    ordering_fields = ['page_id', 'page_name', 'updated_at']
    ordering = ['page_id']
    
    def get_serializer_class(self):
        """Use different serializers for different actions."""
        if self.action in ['create', 'update', 'partial_update']:
            return SEOTagWriteSerializer
        return SEOTagSerializer
    
    @action(detail=False, methods=['get'], url_path='full-seo')
    def full_seo(self, request):
        """
        Get complete SEO data: all page tags + advanced SEO settings.
        GET /api/seo/full-seo/
        
        Response structure:
        {
            "seo_tags": [...],
            "advanced_seo": {...}
        }
        """
        # Get all SEO tags
        seo_tags = self.get_queryset()
        
        # Get or create advanced SEO settings
        advanced_seo = AdvancedSEO.load()
        
        # Prepare response data
        data = {
            'seo_tags': SEOTagSerializer(seo_tags, many=True).data,
            'advanced_seo': AdvancedSEOSerializer(advanced_seo).data
        }
        
        return Response(data)
    
    def perform_create(self, serializer):
        """Track who created the record."""
        serializer.save(
            created_by=self.request.user.username if self.request.user.is_authenticated else ''
        )
    
    def perform_update(self, serializer):
        """Track who updated the record."""
        serializer.save(
            updated_by=self.request.user.username if self.request.user.is_authenticated else ''
        )


class AdvancedSEOViewSet(viewsets.ViewSet):
    """
    ViewSet for site-wide Advanced SEO settings (singleton).
    
    Endpoints:
    - GET   /api/seo/advanced/  - Get advanced SEO settings
    - PUT   /api/seo/advanced/  - Update advanced SEO settings
    - PATCH /api/seo/advanced/  - Partial update advanced SEO
    """
    
    def list(self, request):
        """
        Get advanced SEO settings.
        GET /api/seo/advanced/
        """
        advanced_seo = AdvancedSEO.load()
        serializer = AdvancedSEOSerializer(advanced_seo)
        return Response(serializer.data)
    
    def update(self, request):
        """
        Full update of advanced SEO settings.
        PUT /api/seo/advanced/
        """
        advanced_seo = AdvancedSEO.load()
        serializer = AdvancedSEOSerializer(advanced_seo, data=request.data)
        
        if serializer.is_valid():
            serializer.save(
                updated_by=request.user.username if request.user.is_authenticated else ''
            )
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request):
        """
        Partial update of advanced SEO settings.
        PATCH /api/seo/advanced/
        """
        advanced_seo = AdvancedSEO.load()
        serializer = AdvancedSEOSerializer(advanced_seo, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save(
                updated_by=request.user.username if request.user.is_authenticated else ''
            )
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
