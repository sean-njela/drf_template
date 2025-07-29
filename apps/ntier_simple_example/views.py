# booking/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookingRequestSerializer
from .services import BookingService

class BookingView(APIView):
    """Presentation Layer: handles incoming API requests"""

    def post(self, request) -> Response:
        """
        Handles a POST request to book a property.

        Args:
            request: The incoming HTTP request.

        Returns:
            Response: The API response containing the booking result.
        """
        serializer = BookingRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service = BookingService()
        result = service.book_stay(
            user_id=request.user.id,
            property_id=serializer.validated_data["property_id"],
            start_date=serializer.validated_data["start_date"],
            end_date=serializer.validated_data["end_date"],
        )

        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        return Response(result, status=status.HTTP_201_CREATED)
