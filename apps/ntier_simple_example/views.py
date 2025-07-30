# booking/views.py
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import BookingRequestSerializer, BookingResponseSerializer
from .services import BookingService


@extend_schema(
    request=BookingRequestSerializer,
    responses={
        201: OpenApiResponse(
            response=BookingResponseSerializer,
            description="Successful booking response",
            examples=[
                OpenApiExample(
                    name="Booking Example",
                    value={"booking_id": 101, "total_price": "850.00"}
                )
            ]
        )
    }
)

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
