from django.db import models

class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Booking(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,  on_delete=models.CASCADE) 
    checkin_date = models.DateField()
    chickout_date = models.DateField()
    total_price = models.DecimalField(max_digits=10 , decimal_places=2)

class Payment(models.Model):
    booking_id = models.ForeignKey(Booking,on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method  = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

# class Item(models.Model):
#     name = models.CharField(max_length=200)
#     created = models.DateTimeField(auto_now_add=True)