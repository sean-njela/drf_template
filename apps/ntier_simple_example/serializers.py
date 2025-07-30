# booking/serializers.py
from rest_framework import serializers


class BookingRequestSerializer(serializers.Serializer):
    """
    Serializer for booking requests.
    """

    property_id = serializers.IntegerField()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
