# File: enquiries/apps.py
# 1-line comment: App config for enquiries
from django.apps import AppConfig


class EnquiriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'enquiries'
    verbose_name = 'Enquiries'


