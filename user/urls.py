from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     # path('', views.index, name='home'), 
     path('', views.home, name='home'),
     path('about', views.about, name='about'),
     path('price_details', views.price_details, name='price_details'),
     path('payment', views.payment, name='payment'),
     path('map', views.map, name='map'),
     path('service', views.service, name='service'),
     path('terminal', views.terminal, name='terminal'),
     path('lounge', views.lounge, name='lounge'),
     path('airport', views.airport, name='airport'),
     path('ground', views.ground, name='ground'),
     path('cargo', views.cargo, name='cargo'),
     path('medical', views.medical, name='medical'),
     path('private', views.private, name='private'),
     path('flight_details', views.flight_details, name='flight_details'),
     path('contact', views.contact, name='contact'),
     path('search_by_source', views.search_by_source, name='search_by_source'),
     path('search_by_destination', views.search_by_destination, name='search_by_destination'),
     path('passenger_details', views.passenger_details, name='passenger_details'),
     path('book_flight/<int:pk>', views.book_flight, name='book_flight'),
     # path('create_pdf/<int:pk>', views.create_pdf, name='create_pdf'),
     path('ticket', views.ticket, name='ticket'),
    #  path('view_booking', views.view_booking, name='view_booking'),
    
     path('login', views.loginUser, name='login'),
     path('logout', views.logoutUser, name ='logout'),
]