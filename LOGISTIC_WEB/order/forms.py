from django import forms 
from order.models import Order,Receiving_location,Destination_location,Vehicle,Cargo,Bill


class Order_form(forms.ModelForm):
    class Meta():
        model = Order
        fields = '__all__'

class Receiving_location_form(forms.ModelForm):
    class Meta():
        model = Receiving_location
        fields = '__all__'

class Destination_location_form(forms.ModelForm):
    class Meta():
        model = Destination_location
        fields = '__all__'

class Vehicle_form(forms.ModelForm):
    class Meta():
        model = Vehicle
        fields = '__all__'

class Cargo_form(forms.ModelForm):
    class Meta():
        model = Cargo
        fields = '__all__'

class Bill_form(forms.ModelForm):
    class Meta():
        model = Bill
        fields = '__all__'