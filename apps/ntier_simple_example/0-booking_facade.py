from abc import ABC, abstractmethod
from .services import BookingService


class BookingFacade(ABC):
    """
    BookingFacade interface.
    Ensures that we do not expose the inner workings of the system to external clients.
    It only calls the services and returns the result.
    """
    @abstractmethod
    def create_booking(self, user, data):
        """
        Creates a new booking.

        Args:
            user: The user making the booking.
            data: The booking data.

        Returns:
            Booking: The created booking object.
        """
        service = BookingService()
        return service.book_stay(user_id=user.id, **data)

    @abstractmethod
    def cancel_booking(self, booking_id):
        """
        Cancels a booking.

        Args:
            booking_id: The ID of the booking to cancel.
        """
        # service = BookingService()
        # return service.cancel_booking(booking_id)

    @abstractmethod
    def get_booking_summary(self, user_id):
        """
        Gets a summary of the user's bookings.

        Args:
            user_id: The ID of the user.

        Returns:
            list: A list of booking summaries.
        """
        # service = BookingService()
        # return service.get_booking_summary(user_id)


# Used in another module like this:

# # users/services.py
# from apps.ntier_simple_example.0-booking_facade import BookingInterface

# def register_and_book(user_data, property_id, date):
#     user = create_user(user_data)
#     return BookingInterface.book_stay(user.id, property_id, date)
