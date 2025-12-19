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

class DownloadBrochureViewSet(PublicCreateAdminCRUDViewSet):
    queryset = models.DownloadBrochure.objects.all().order_by('-created_at')
    serializer_class = serializers.DownloadBrochureSerializer


