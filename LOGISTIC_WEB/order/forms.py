from django import forms 
from order.models import Order,Receiving_location,Destination_location,Vehicle,Cargo,Bill


class Order_form(forms.ModelForm):
    class Meta():
        model = Order
        fields = '__all__'

class Receiving_location_form(forms.ModelForm):
    class Meta():
        model = Receiving_location
        fields = ('company_name','company_number','address','pickup_date')

class Destination_location_form(forms.ModelForm):
    class Meta():
        model = Destination_location
        fields = ('company_name','company_number','address','pickup_date')

class Vehicle_form(forms.ModelForm):
    class Meta():
        model = Vehicle
        fields = ('type','price_km','max_weight','storage_height','storage_width','storage_length')

class Cargo_form(forms.ModelForm):
    class Meta():
        model = Cargo
        fields = ('type','weight','height','width','length','image')

class Bill_form(forms.ModelForm):
    class Meta():
        model = Bill
        fields = ('company_name','address','name','surname','email','satis_vergisi_kimligi')