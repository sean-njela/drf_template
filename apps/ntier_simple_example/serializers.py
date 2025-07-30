# booking/serializers.py
from rest_framework import serializers


class BookingRequestSerializer(serializers.Serializer):
    """
    Serializer for booking requests.
    """

    property_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()

class BookingResponseSerializer(serializers.Serializer):
    booking_id = serializers.IntegerField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)
