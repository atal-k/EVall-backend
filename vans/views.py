from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Van
from .serializers import VanSerializer

class VanViewSet(viewsets.ModelViewSet):
    queryset = Van.objects.all()
    serializer_class = VanSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status', 'charging_type', 'is_featured']
    search_fields = ['name', 'tagline']
    ordering_fields = ['price', 'range_km', 'created_at']
    
    @action(detail=True, methods=['post'])
    def toggle_wishlist(self, request, pk=None):
        """Toggle wishlist status"""
        van = self.get_object()
        van.is_wishlisted = not van.is_wishlisted
        van.save()
        serializer = self.get_serializer(van)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get van counts by category"""
        return Response({
            'lightDuty': Van.objects.filter(category='light-duty').count(),
            'mediumDuty': Van.objects.filter(category='medium-duty').count(),
            'heavyDuty': Van.objects.filter(category='heavy-duty').count(),
        })