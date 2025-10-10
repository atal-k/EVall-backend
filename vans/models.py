from django.db import models

class Van(models.Model):
    CATEGORY_CHOICES = [
        ('light-duty', 'Light Duty'),
        ('medium-duty', 'Medium Duty'),
        ('heavy-duty', 'Heavy Duty'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('pre-order', 'Pre-Order'),
    ]
    CHARGING_CHOICES = [
        ('fast', 'Fast'),
        ('standard', 'Standard'),
    ]
    
    # Basic info
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    tagline = models.CharField(max_length=200)
    images = models.JSONField(default=list)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    badge = models.CharField(max_length=20, blank=True)
    badge_color = models.CharField(max_length=20, blank=True)
    
    # Specs
    charging_type = models.CharField(max_length=20, choices=CHARGING_CHOICES, default='fast')
    range_km = models.PositiveIntegerField(help_text="Range in kilometers")
    power_kw = models.PositiveIntegerField(help_text="Power in kilowatts")
    battery_capacity_kwh = models.PositiveIntegerField(help_text="Battery capacity in kWh")
    payload_ton = models.DecimalField(max_digits=4, decimal_places=1, help_text="Payload in tons")
    
    # Pricing & features
    price = models.PositiveIntegerField(help_text="Price in rupees")
    currency = models.CharField(max_length=5, default='₹')
    is_featured = models.BooleanField(default=False)
    is_wishlisted = models.BooleanField(default=False)
    
    # Timestamps (good practice!)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_at']  # Oldest first
        verbose_name_plural = "Vans"
    
    def __str__(self):
        return f"{self.name} ({self.category})"