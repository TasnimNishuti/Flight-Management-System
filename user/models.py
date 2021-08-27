from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
import django.utils.timezone

# Create your models here.
class Flight(models.Model):
    flight_no = models.IntegerField(primary_key=True, default=1007)
    flight_id = models.TextField(null=True)
    airline_name = models.CharField(max_length=50)
    no_of_seats = models.IntegerField(default=0)
    source = models.CharField(max_length=50)
    source_code = models.CharField(max_length=3)
    destination = models.CharField(max_length=50)
    destination_code = models.CharField(max_length=3)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    
class Passenger(models.Model):
    pnr = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(null=True)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE, default=1007)
    mobile =  models.IntegerField(null=True)
    address = models.TextField(null=True)
    passport_no = models.TextField(null=True)
    ticket_class = models.TextField(null=True)
    seats = models.IntegerField(default=1)
    pay_option =  models.TextField(null=True)
    name_card = models.TextField(null=True)
    card_no = models.IntegerField(null=True)
    expiration = models.DateField(null=True)
    cvv =  models.IntegerField(null=True)
    amount =  models.IntegerField(null=True)