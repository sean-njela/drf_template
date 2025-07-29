# booking/repositories.py
from .models import Property, Booking

class PropertyRepo:
    """
    Repository for property data.
    """
    @staticmethod
    def get_by_id(property_id) -> Property | None:
        """
        Retrieves a property by its ID.

        Args:
            property_id: The ID of the property to retrieve.

        Returns:
            Property | None: The property object if found, None otherwise.
        """
        try:
            return Property.objects.prefetch_related("reservations").get(id=property_id)
        except Property.DoesNotExist:
            return None

class BookingRepo:
    """
    Repository for booking data.
    """
    @staticmethod
    def create(user_id, property_id, start_date, end_date, price) -> Booking | None:
        """
        Creates a new booking.

        Args:
            user_id: The ID of the user making the booking.
            property_id: The ID of the property to book.
            start_date: The start date of the booking.
            end_date: The end date of the booking.
            price: The total price for the booking.

        Returns:
            Booking | None: The created booking object if successful, None otherwise.
        """
        try:
            return Booking.objects.create(
                user_id=user_id,
                property_id=property_id,
                start_date=start_date,
                end_date=end_date,
                price=price,
            )
        except Exception as e:
            return None
