# booking/tests/test_services.py
from django.test import TestCase
from booking.models import Property, Booking
from booking.services import BookingService
from django.contrib.auth import get_user_model

User = get_user_model()

class BookingServiceTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="u", password="p")
        self.property = Property.objects.create(owner=self.user, title="Cabin", price_per_night=80)

    def test_booking_success(self):
        service = BookingService()
        result = service.book_stay(
            user_id=self.user.id,
            property_id=self.property.id,
            start_date="2025-08-01",
            end_date="2025-08-03"
        )
        self.assertTrue(result.get("success"))
        self.assertGreater(result.get("total_price", 0), 0)

