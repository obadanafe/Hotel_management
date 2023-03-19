from django.urls import path
from . import views 

urlpatterns = [
    path('rooms', views.getRooms),
    path('customers/', views.getCustomers),
    path('bookings/', views.getBooking),
    path('payments/', views.getPayments),
]
