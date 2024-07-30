from django.contrib import admin
from order.models import Order,Receiving_location,Destination_location,Vehicle,Cargo,Bill

admin.site.register(Order)
admin.site.register(Receiving_location)
admin.site.register(Destination_location)
admin.site.register(Vehicle)
admin.site.register(Cargo)
admin.site.register(Bill)
