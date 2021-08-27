from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import  Flight, Passenger

admin.site.register(Flight),
admin.site.register(Passenger)
