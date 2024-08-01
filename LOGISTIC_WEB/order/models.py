from django.db import models
from django.utils import timezone
import uuid

class Order(models.Model):
    order_code = models.CharField(max_length=10, default=uuid.uuid4, unique=True, editable=False)
    customer = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status = models.CharField(max_length=30) # Sipariş aktif,pasif,tamamlanmış,iptal...
    price = models.IntegerField()
    creation_date = models.DateTimeField(default=timezone.now)

class Receiving_location(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='Receiving_location')
    company_name = models.CharField(max_length=200)
    company_number = models.CharField(max_length=12)
    address = models.TextField()
    pickup_date = models.DateTimeField()

class Destination_location(models.Model): # Durak yerine bu sınıfı kullanacağız
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='Destination_location')
    company_name = models.CharField(max_length=200)
    company_number = models.CharField(max_length=12)
    address = models.TextField()
    pickup_date = models.DateTimeField()

class Vehicle(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='Vehicle')
    type = models.CharField(max_length=30) # doblo, kamyon, tır vs. yada direkt aracın ismi olarak kullanırız 
    price_km = models.IntegerField()
    max_weight = models.IntegerField()
    storage_height = models.IntegerField() # santimetre cinsinden
    storage_width = models.IntegerField()
    storage_length = models.IntegerField()

class Cargo(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='Cargo')
    type = models.CharField(max_length=30) # elma,armut,tabak taşınacak maddenin ismi /// opsiyonel
    weight = models.IntegerField()
    height = models.IntegerField()
    width =models.IntegerField()
    length = models.IntegerField()
    image = models.ImageField(upload_to='cargo_images',blank=True,null=True)

class Bill(models.Model): # fatura bilgiler
    order = models.OneToOneField(Order,on_delete=models.PROTECT)
    company_name = models.CharField(max_length=200)
    address = models.TextField()
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    satis_vergisi_kimligi = models.CharField(max_length=200)  # Ne olduğunu anlamadım