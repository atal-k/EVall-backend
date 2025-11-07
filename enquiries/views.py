# File: enquiries/views.py
# 1-line comment: DRF viewsets exposing create + admin CRUD
from rest_framework import viewsets, permissions
from . import models, serializers


class PublicCreateAdminCRUDViewSet(viewsets.ModelViewSet):
    """
    Generic viewset: create() is public (AllowAny) while other actions require admin.
    Child classes should set `queryset` and `serializer_class`.
    """

    def get_permissions(self):
        # Allow unauthenticated users to create resources, but require admin for other actions
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [perm() for perm in permission_classes]


class CustomerSupportViewSet(PublicCreateAdminCRUDViewSet):
    queryset = models.CustomerSupport.objects.all().order_by('-created_at')
    serializer_class = serializers.CustomerSupportSerializer


class RequestDemoViewSet(PublicCreateAdminCRUDViewSet):
    queryset = models.RequestDemo.objects.all().order_by('-created_at')
    serializer_class = serializers.RequestDemoSerializer


class DealershipEnquiryViewSet(PublicCreateAdminCRUDViewSet):
    queryset = models.DealershipEnquiry.objects.all().order_by('-created_at')
    serializer_class = serializers.DealershipEnquirySerializer


class CustomerFeedbackViewSet(PublicCreateAdminCRUDViewSet):
    queryset = models.CustomerFeedback.objects.all().order_by('-created_at')
    serializer_class = serializers.CustomerFeedbackSerializer


class TestDriveBookingViewSet(PublicCreateAdminCRUDViewSet):
    queryset = models.TestDriveBooking.objects.all().order_by('-created_at')
    serializer_class = serializers.TestDriveBookingSerializer


# File: enquiries/urls.py
# 1-line comment: Router registrations for all endpoints
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerSupportViewSet,
    RequestDemoViewSet,
    DealershipEnquiryViewSet,
    CustomerFeedbackViewSet,
    TestDriveBookingViewSet,
)

router = DefaultRouter()
# Register each base path so endpoints appear as /api/<basename>/
router.register(r'customer-support', CustomerSupportViewSet, basename='customer-support')
router.register(r'request-demo', RequestDemoViewSet, basename='request-demo')
router.register(r'dealership-enquiry', DealershipEnquiryViewSet, basename='dealership-enquiry')
router.register(r'feedback', CustomerFeedbackViewSet, basename='feedback')
router.register(r'testdrive-booking', TestDriveBookingViewSet, basename='testdrive-booking')

urlpatterns = [
    path('', include(router.urls)),
]