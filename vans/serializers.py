from rest_framework import serializers
from .models import Van

class VanSerializer(serializers.ModelSerializer):
    specs = serializers.SerializerMethodField()
    
    class Meta:
        model = Van
        fields = [
            'id', 'name', 'category', 'tagline', 'images', 
            'status', 'badge', 'badge_color', 'charging_type',
            'price', 'currency', 'is_featured', 'is_wishlisted',
            'specs'
        ]
    
    def get_specs(self, obj):
        """Transform specs to match your React component structure"""
        return {
            'range': obj.range_km,
            'power': obj.power_kw,
            'battery': obj.battery_capacity_kwh,
            'payload': float(obj.payload_ton)
        }