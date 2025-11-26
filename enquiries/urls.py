# enquiries/urls.py
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerSupportViewSet,
    RequestDemoViewSet,
    DealershipEnquiryViewSet,
    CustomerFeedbackViewSet,
    TestDriveBookingViewSet,
)

router = DefaultRouter()
router.register(r'customer-support', CustomerSupportViewSet, basename='customer-support')
router.register(r'request-demo', RequestDemoViewSet, basename='request-demo')
router.register(r'dealership-enquiry', DealershipEnquiryViewSet, basename='dealership-enquiry')
router.register(r'feedback', CustomerFeedbackViewSet, basename='feedback')
router.register(r'testdrive-booking', TestDriveBookingViewSet, basename='testdrive-booking')

urlpatterns = router.urls