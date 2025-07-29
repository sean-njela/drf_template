# booking/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Property(models.Model):
    """
    Property model.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """
    Booking model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="reservations")
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def overlaps(self, start_date, end_date) -> bool:
        """
        Checks if the booking overlaps with the given date range.

        Args:
            start_date: The start date of the booking.
            end_date: The end date of the booking.

        Returns:
            bool: True if the booking overlaps, False otherwise.
        """
        return not (self.end_date < start_date or self.start_date > end_date)

