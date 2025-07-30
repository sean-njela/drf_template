# booking/services.py
from .domain import BookingRules
from .repositories import BookingRepo, PropertyRepo


class BookingService:
    """Application Layer: Orchestrates property booking."""

    def book_stay(self, user_id, property_id, start_date, end_date) -> dict:
        """
        Orchestrates the booking process.

        Args:
            user_id: The ID of the user making the booking.
            property_id: The ID of the property to book.
            start_date: The start date of the booking.
            end_date: The end date of the booking.

        Returns:
            dict: The booking result containing success status and booking details.
        """
        property_data = PropertyRepo.get_by_id(property_id)
        if not property_data:
            return {"error": "Property not found."}

        if not BookingRules.is_available(property_data, start_date, end_date):
            return {"error": "Property not available."}

        price = BookingRules.calculate_price(property_data, start_date, end_date)

        booking = BookingRepo.create(user_id, property_id, start_date, end_date, price)
        return {"success": True, "booking_id": booking.id, "total_price": price}
