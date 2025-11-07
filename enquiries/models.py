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

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    contact_number = models.CharField(max_length=64)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    vehicle_type = models.PositiveSmallIntegerField(default=1)
    message = models.TextField(null=True, blank=True)
    consent1 = models.BooleanField(default=False)
    consent2 = models.BooleanField(default=False)
    raw_payload = JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"CustomerSupport({self.id}) - {self.name}"


class RequestDemo(TimeStampedModel):
    """Stores data submitted via /api/request-demo"""

    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=64)
    alternate_number = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)

    vehicle_types = JSONField(default=list, blank=True)  # list of selected vehicle types
    vehicle_other = models.CharField(max_length=255, null=True, blank=True)

    applications = JSONField(default=list, blank=True)
    application_other = models.CharField(max_length=255, null=True, blank=True)

    fleet_size = models.CharField(max_length=128, null=True, blank=True)
    timeline = models.CharField(max_length=128, null=True, blank=True)
    procurement_mode = models.CharField(max_length=128, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    consent = models.BooleanField(default=False)
    requested_date = models.DateField(null=True, blank=True)

    raw_payload = JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"RequestDemo({self.id}) - {self.name}"


class DealershipEnquiry(TimeStampedModel):
    """Stores data submitted via /api/dealership-enquiry"""

    # Personal details
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    pincode = models.CharField(max_length=20, null=True, blank=True)
    contact_number = models.CharField(max_length=64)
    alternate_number = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)

    # Business details
    current_business = models.CharField(max_length=255, null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    proposed_territory = models.CharField(max_length=255, null=True, blank=True)
    firm_turnover = models.BigIntegerField(null=True, blank=True)
    investment_capacity = models.BigIntegerField(null=True, blank=True)
    infrastructure = JSONField(default=list, blank=True)  # array of infrastructure items
    reason_for_interest = models.TextField(null=True, blank=True)

    other_info = models.TextField(null=True, blank=True)
    raw_payload = JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"DealershipEnquiry({self.id}) - {self.name}"


class CustomerFeedback(TimeStampedModel):
    """Stores feedback submitted via /api/feedback"""

    # Customer details
    name = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)

    # Vehicle details
    model_name = models.CharField(max_length=255, null=True, blank=True)
    vehicle_type = models.PositiveSmallIntegerField(null=True, blank=True)

    # Ratings / performance and experiences stored as JSON for flexibility
    vehicle_performance = JSONField(default=dict, blank=True)
    sales_service_experience = JSONField(default=dict, blank=True)
    open_feedback = JSONField(default=dict, blank=True)

    raw_payload = JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"CustomerFeedback({self.id}) - {self.name or 'anonymous'}"


class TestDriveBooking(TimeStampedModel):
    """Stores test drive booking data submitted via /api/testdrive-booking"""

    # Customer details
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=64)
    email = models.EmailField(null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)

    # Preferences
    selected_models = JSONField(default=list, blank=True)
    other_model = models.CharField(max_length=255, null=True, blank=True)
    preferred_time_slot = models.CharField(max_length=128, null=True, blank=True)

    business_segment = models.CharField(max_length=255, null=True, blank=True)
    business_segment_other = models.CharField(max_length=255, null=True, blank=True)

    consent = models.BooleanField(default=False)
    test_drive_date = models.DateField(null=True, blank=True)

    raw_payload = JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"TestDriveBooking({self.id}) - {self.name}"