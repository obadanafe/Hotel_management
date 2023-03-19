from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Room, Customer, Booking, Payment
from .serializers import RoomSerializer, CustomerSerializer, BookingSerializer, PaymentSerializer

@api_view(['GET'])
def getRooms(request): 
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCustomers(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBooking(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPayments(request):
    payments = Payment.objects.all()
    serializer = PaymentSerializer(payments, many=True)
    return Response(serializer.data)



#@api_view(['POST'])