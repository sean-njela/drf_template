# booking/domain.py


class BookingRules:
    """Domain Layer: Core business logic. No Django or DRF."""

    @staticmethod
    def is_available(property_data, start_date, end_date) -> bool:
        """
        Checks if the property is available for the given date range.

        Args:
            property_data: The property data.
            start_date: The start date of the booking.
            end_date: The end date of the booking.

        Returns:
            bool: True if the property is available, False otherwise.
        """
        for reservation in property_data.reservations.all():
            if reservation.overlaps(start_date, end_date):
                return False
        return True

    @staticmethod
    def calculate_price(property_data, start_date, end_date) -> int:
        """
        Calculates the total price for the booking.

        Args:
            property_data: The property data.
            start_date: The start date of the booking.
            end_date: The end date of the booking.

        Returns:
            int: The total price for the booking.
        """
        days = max(1, (end_date - start_date).days)
        return days * property_data.price_per_night
