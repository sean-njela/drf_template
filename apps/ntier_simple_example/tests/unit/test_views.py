# booking/tests/test_views.py
from django.contrib.auth import get_user_model
from django.urls import reverse
from ntier_simple_example.models import Property
from rest_framework.test import APITestCase

User = get_user_model()


class BookingViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass")
        self.property = Property.objects.create(
            owner=self.user,
            title="Beach House",
            price_per_night=100,
        )
        self.client.force_authenticate(self.user)

    def test_successful_booking(self):
        url = reverse("book-property")
        data = {
            "property_id": self.property.id,
            "start_date": "2025-08-01",
            "end_date": "2025-08-05",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("booking_id", response.data)
