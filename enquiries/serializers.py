# File: enquiries/serializers.py
# 1-line comment: DRF serializers for validation & transformation
from rest_framework import serializers
from . import models
from datetime import datetime


class CustomerSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerSupport
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_contact_number(self, value):
        # Basic sanity check — ensure not empty
        if not value:
            raise serializers.ValidationError('contactNumber is required')
        return value


class RequestDemoSerializer(serializers.ModelSerializer):
    requested_date = serializers.DateField(required=False, allow_null=True, input_formats=['%Y-%m-%d'])

    class Meta:
        model = models.RequestDemo
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_vehicle_types(self, value):
        if value is None:
            return []
        if not isinstance(value, (list, tuple)):
            raise serializers.ValidationError('vehicleTypes must be a list')
        return list(value)

    def validate_applications(self, value):
        if value is None:
            return []
        if not isinstance(value, (list, tuple)):
            raise serializers.ValidationError('applications must be a list')
        return list(value)


class DealershipEnquirySerializer(serializers.ModelSerializer):
    infrastructure = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = models.DealershipEnquiry
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_experience(self, value):
        if value is None:
            return value
        if value < 0:
            raise serializers.ValidationError('experience must be >= 0')
        return value


class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerFeedback
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_vehicle_performance(self, value):
        if value is None:
            return {}
        if not isinstance(value, dict):
            raise serializers.ValidationError('vehiclePerformance must be an object')
        return value


class TestDriveBookingSerializer(serializers.ModelSerializer):
    test_drive_date = serializers.DateField(required=False, allow_null=True, input_formats=['%Y-%m-%d'])

    class Meta:
        model = models.TestDriveBooking
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_selected_models(self, value):
        if value is None:
            return []
        if not isinstance(value, (list, tuple)):
            raise serializers.ValidationError('selectedModels must be a list')
        return list(value)