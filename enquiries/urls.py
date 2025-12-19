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
    DownloadBrochureViewSet,
)

router = DefaultRouter()
# Register each base path so endpoints appear as /api/<basename>/
router.register(r'customer-support', CustomerSupportViewSet, basename='customer-support')
router.register(r'request-demo', RequestDemoViewSet, basename='request-demo')
router.register(r'dealership-enquiry', DealershipEnquiryViewSet, basename='dealership-enquiry')
router.register(r'feedback', CustomerFeedbackViewSet, basename='feedback')
router.register(r'testdrive-booking', TestDriveBookingViewSet, basename='testdrive-booking')
router.register(r'download-brochure', DownloadBrochureViewSet, basename='download-brochure')

urlpatterns = [
    path('', include(router.urls)),
]