from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VanViewSet

router = DefaultRouter()
router.register(r'vans', VanViewSet, basename='van')

urlpatterns = [
    path('', include(router.urls)),
]