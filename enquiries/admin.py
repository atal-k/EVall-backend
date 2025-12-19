# File: enquiries/admin.py
# 1-line comment: Register models with Django admin
from django.contrib import admin
from . import models


@admin.register(models.CustomerSupport)
class CustomerSupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_number', 'created_at')
    readonly_fields = ('raw_payload', 'created_at', 'updated_at')


@admin.register(models.RequestDemo)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company_name', 'contact_number', 'requested_date', 'created_at')
    readonly_fields = ('raw_payload', 'created_at', 'updated_at')


@admin.register(models.DealershipEnquiry)
class DealershipEnquiryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company_name', 'contact_number', 'created_at')
    readonly_fields = ('raw_payload', 'created_at', 'updated_at')


@admin.register(models.CustomerFeedback)
class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    readonly_fields = ('raw_payload', 'created_at', 'updated_at')


@admin.register(models.TestDriveBooking)
class TestDriveBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_number', 'test_drive_date', 'created_at')
    readonly_fields = ('raw_payload', 'created_at', 'updated_at')

@admin.register(models.DownloadBrochure)
class DownloadBrochureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company_name', 'contact_number', 'email', 'created_at')
    readonly_fields = ('raw_payload', 'created_at', 'updated_at')