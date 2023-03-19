from rest_framework import serializers
from .models import Room, Customer, Booking, Payment

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'price', 'is_available']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name',  'email','phone', 'address']

class BookingSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    room = RoomSerializer()
    class Meta:
        model = Booking
        fields = ['id', 'room', 'customer', 'checkin_date', 'checkout_date', 'total_payment']

class PaymentSerializer(serializers.ModelSerializer):
    booking = BookingSerializer()
    class Meta:
        model = Payment
        fields = ['id', 'booking', 'payment_date', 'Payment_method', 'amount']
