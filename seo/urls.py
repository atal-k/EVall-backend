# ============================================================================
# FILE: seo/urls.py
# ============================================================================
"""
URL routing for SEO Tags API endpoints.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SEOTagViewSet, AdvancedSEOViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'seo', SEOTagViewSet, basename='seo')

app_name = 'seo'

urlpatterns = [
    # SEO Tags endpoints (via router)
    path('', include(router.urls)),
    
    # Advanced SEO endpoints (manual routes for singleton)
    path('seo/advanced/', AdvancedSEOViewSet.as_view({
        'get': 'list',
        'put': 'update',
        'patch': 'partial_update'
    }), name='advanced-seo'),
]