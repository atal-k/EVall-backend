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
    email = models.EmailField()
    contact_number = models.CharField(max_length=64)
    company_name = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=128, )
    city = models.CharField(max_length=128, )
    vehicle_type = models.PositiveSmallIntegerField()
    message = models.TextField()
    consent1 = models.BooleanField(default=False)
    consent2 = models.BooleanField(default=False)
    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"CustomerSupport({self.id}) - {self.name}"


class RequestDemo(TimeStampedModel):
    """Stores data submitted via /api/request-demo"""

    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=64)
    alternate_number = models.CharField(max_length=64, null=True)
    email = models.EmailField()

    address = models.TextField()
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)

    vehicle_types = JSONField(default=list)  # list of selected vehicle types
    vehicle_other = models.CharField(max_length=255, null=True)

    applications = JSONField(default=list)
    application_other = models.CharField(max_length=255, null=True)

    fleet_size = models.CharField(max_length=128)
    timeline = models.CharField(max_length=128)
    procurement_mode = models.CharField(max_length=128)
    additional_info = models.TextField(null=True)

    consent = models.BooleanField(default=False)
    requested_date = models.DateField()

    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"RequestDemo({self.id}) - {self.name}"


class DealershipEnquiry(TimeStampedModel):
    """Stores data submitted via /api/dealership-enquiry"""

    # Personal details
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    pincode = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=64)
    alternate_number = models.CharField(max_length=64, null=True)
    email = models.EmailField()
    website = models.CharField(max_length=255, null=True)

    # Business details
    current_business = models.CharField(max_length=255)
    experience = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    proposed_territory = models.CharField(max_length=255)
    firm_turnover = models.BigIntegerField()
    investment_capacity = models.BigIntegerField()
    infrastructure = JSONField(default=list)
    reason_for_interest = models.TextField()

    other_info = models.TextField(null=True)
    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"DealershipEnquiry({self.id}) - {self.name}"


class CustomerFeedback(TimeStampedModel):
    """Stores feedback submitted via /api/feedback"""

    # Customer details
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True)
    contact_number = models.CharField(max_length=64)
    email = models.EmailField()
    state = models.CharField(max_length=128, )
    city = models.CharField(max_length=128, )

    # Vehicle details
    model_name = models.CharField(max_length=255, )
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
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, null=True)
    contact_number = models.CharField(max_length=64)
    email = models.EmailField()
    state = models.CharField(max_length=128)
    city = models.CharField(max_length=128)

    # Preferences
    selected_models = JSONField(default=list)
    other_model = models.CharField(max_length=255, null=True)
    time_slot = models.CharField(max_length=128)

    business_segment = models.CharField(max_length=255)
    business_segment_other = models.CharField(max_length=255, null=True)

    consent = models.BooleanField(default=False)
    test_drive_date = models.DateField()

    raw_payload = JSONField(null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"TestDriveBooking({self.id}) - {self.name}"