# apps/ntier_simple_example/admin.py
from django.contrib import admin
from .models import Booking, Property

admin.site.register(Property)
admin.site.register(Booking)
