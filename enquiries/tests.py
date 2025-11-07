# File: enquiries/tests.py
# 1-line comment: Basic API tests for create endpoints
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from . import models


class PublicCreateTests(APITestCase):

    def test_create_customer_support(self):
        url = reverse('customer-support-list')
        payload = {
            "name": "John Doe",
            "email": "john@example.com",
            "contact_number": "+91-9876543210",
            "company_name": "Acme",
            "state": "Karnataka",
            "city": "Bangalore",
            "vehicle_type": 2,
            "message": "Help needed",
            "consent1": True,
            "consent2": False,
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.CustomerSupport.objects.count(), 1)

    def test_create_request_demo(self):
        url = reverse('request-demo-list')
        payload = {
            "name": "Demo User",
            "contact_number": "+91-9999999999",
            "vehicle_types": ["van", "truck"],
            "applications": ["delivery"],
            "consent": True,
            "date": "2025-01-01",
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.RequestDemo.objects.count(), 1)

    def test_create_dealership_enquiry(self):
        url = reverse('dealership-enquiry-list')
        payload = {
            "name": "Dealer One",
            "contact_number": "+91-8888888888",
            "experience": 5,
            "infrastructure": ["workshop", "showroom"],
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.DealershipEnquiry.objects.count(), 1)

    def test_create_feedback(self):
        url = reverse('feedback-list')
        payload = {
            "customerDetails": {
                "name": "Alice",
                "contactNumber": "+91-7777777777",
            },
            "vehicleDetails": {
                "modelName": "VAN-X",
                "vehicleType": 1,
            },
            "vehiclePerformance": {
                "drivingExperience": "good"
            }
        }
        # Our serializer expects flat fields as described in the model; the frontend hooks transform data
        # But to ensure API accepts the shape saved in models, pass flattened payload matching serializer
        payload_flat = {
            "name": "Alice",
            "contact_number": "+91-7777777777",
            "model_name": "VAN-X",
            "vehicle_performance": {"drivingExperience": "good"}
        }
        response = self.client.post(url, payload_flat, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.CustomerFeedback.objects.count(), 1)

    def test_create_testdrive_booking(self):
        url = reverse('testdrive-booking-list')
        payload = {
            "name": "Booker",
            "contact_number": "+91-6666666666",
            "selected_models": ["VAN-X"],
            "preferred_time_slot": "10:00-12:00",
            "test_drive_date": "2025-02-14"
        }
        response = self.client.post(url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.TestDriveBooking.objects.count(), 1)