# ============================================================================
# FILE: blogs/urls.py
# ============================================================================
"""
URL routing for blog API endpoints.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet

# Create router and register viewsets
router = DefaultRouter()
router.register(r'blogs', BlogPostViewSet, basename='blog')

app_name = 'blogs'

urlpatterns = [
    path('', include(router.urls)),
]