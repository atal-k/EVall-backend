# File: enquiries/models.py
# 1-line comment: Models for all five form-based resources
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

# JSONField is available in Django core starting Django 3.1+
try:
    from django.db.models import JSONField
except Exception:
    # fallback for older versions (not expected for Django 5.2)
    from django.contrib.postgres.fields import JSONField


class TimeStampedModel(models.Model):
    """Abstract base model adding created/updated timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CustomerSupport(TimeStampedModel):
    """Stores data submitted via /api/customer-support"""

    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    contact_number = models.CharField(max_length=64, null=True)
    company_name = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=128, null=True)
    vehicle_type = models.CharField(max_length=255, null=True)
    message = models.TextField(null=True)
    consent1 = models.BooleanField(default=False)
    consent2 = models.BooleanField(default=False)
    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"CustomerSupport({self.id}) - {self.name}"


class RequestDemo(TimeStampedModel):
    """Stores data submitted via /api/request-demo"""

    name = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    designation = models.CharField(max_length=255, null=True)
    contact_number = models.CharField(max_length=64, null=True)
    alternate_number = models.CharField(max_length=64, null=True)
    email = models.EmailField(null=True)

    address = models.TextField(null=True)
    city = models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=128, null=True)

    vehicle_types = JSONField(default=list)  # list of selected vehicle types
    vehicle_other = models.CharField(max_length=255, null=True)

    applications = JSONField(default=list)
    application_other = models.CharField(max_length=255, null=True)

    fleet_size = models.CharField(max_length=128, null=True)
    timeline = models.CharField(max_length=128, null=True)
    procurement_mode = models.CharField(max_length=128, null=True)
    additional_info = models.TextField(null=True)

    consent = models.BooleanField(default=False)
    requested_date = models.DateField(null=True)

    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"RequestDemo({self.id}) - {self.name}"


class DealershipEnquiry(TimeStampedModel):
    """Stores data submitted via /api/dealership-enquiry"""

    # Personal details
    name = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=128, null=True)
    state = models.CharField(max_length=128, null=True)
    pincode = models.CharField(max_length=20, null=True)
    contact_number = models.CharField(max_length=64, null=True)
    alternate_number = models.CharField(max_length=64, null=True)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=255, null=True)

    # Business details
    current_business = models.CharField(max_length=255, null=True)
    experience = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=True)
    proposed_territory = models.CharField(max_length=255, null=True)
    firm_turnover = models.BigIntegerField(null=True)
    investment_capacity = models.BigIntegerField(null=True)
    infrastructure = JSONField(default=list)
    reason_for_interest = models.TextField(null=True)

    other_info = models.TextField(null=True)
    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"DealershipEnquiry({self.id}) - {self.name}"


class CustomerFeedback(TimeStampedModel):
    """Stores feedback submitted via /api/feedback"""

    # Customer details
    name = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    contact_number = models.CharField(max_length=64, null=True)
    email = models.EmailField(null=True)
    state = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=128, null=True)

    # Vehicle details
    model_name = models.CharField(max_length=255, null=True)
    vehicle_type = models.CharField(max_length=255, null=True)
    vehicle_other = models.CharField(max_length=255, null=True)

    # Ratings / performance and experiences stored as JSON for flexibility
    vehicle_performance = JSONField(default=dict)
    sales_service_experience = JSONField(default=dict)
    open_feedback = JSONField(default=dict)

    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"CustomerFeedback({self.id}) - {self.name or 'anonymous'}"


class TestDriveBooking(TimeStampedModel):
    """Stores test drive booking data submitted via /api/testdrive-booking"""

    # Customer details
    name = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    contact_number = models.CharField(max_length=64, null=True)
    email = models.EmailField(null=True)
    state = models.CharField(max_length=128, null=True)
    city = models.CharField(max_length=128, null=True)

    # Preferences
    vehicle_types = JSONField(default=list)  # list of selected vehicle types
    vehicle_other = models.CharField(max_length=255, null=True)
    time_slot = models.CharField(max_length=128, null=True)

    business_segment = models.CharField(max_length=255, null=True)
    business_segment_other = models.CharField(max_length=255, null=True)

    consent = models.BooleanField(default=False)
    test_drive_date = models.DateField(null=True)

    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"TestDriveBooking({self.id}) - {self.name}"

class DownloadBrochure(TimeStampedModel):
    """Stores test drive booking data submitted via /api/download-brochure"""

    # Customer details
    name = models.CharField(max_length=255, null=True)
    company_name = models.CharField(max_length=255, null=True)
    contact_number = models.CharField(max_length=64, null=True)
    email = models.EmailField(null=True)
    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"DownloadBrochure({self.id}) - {self.name}"