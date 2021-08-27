from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Flight, Passenger
import datetime
import pdfkit
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def index(request):
#     # if request.user.is_anonymous:
#         # return redirect("/login")
#     return render(request, 'index.html')

def home(request):
    # if request.user.is_anonymous:
        # return redirect("/login")
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def map(request):
    return render(request, 'map.html') 

def price_details(request):
    return render(request, 'price_details.html')   

def payment(request):
    return render(request, 'payment.html')     


     
def service(request):
    return render(request, 'service.html')

def terminal(request):
    return render(request, 'terminal.html')  

def lounge(request):
    return render(request, 'lounge.html')  


def airport(request):
    return render(request, 'airport.html') 

def ground(request):
    return render(request, 'ground.html') 

def cargo(request):
    return render(request, 'cargo.html')  

def medical(request):
    return render(request, 'medical.html') 

def private(request):
    return render(request, 'private.html')   
  

def ticket(request):
    return render(request, 'ticket.html') 

# def flight_details(request):
#     return render(request, 'flight_details.html')
#     #  return HttpResponse("this is service page") 
def flight_details(request):
    data = Flight.objects.all()
    return render(request, 'flight_details.html', {'flights': data})
    
def passenger_details(request):
    passenger = Passenger.objects.all()
    if request.user.is_anonymous:
         return redirect("/login")
    return render(request, 'passenger_details.html', {'passenger': passenger})
     
def contact(request):
     return HttpResponse("this is contact page") 

def search_by_source(request):
    if request.method == "POST":
        source = request.POST['source']
        if source:
            data = Flight.objects.filter(source=source)
            return render(request, 'flight_details.html', {'flights': data})
        else:
             return redirect('flight_details')       
    else:
        return redirect('flight_details')


def search_by_destination(request):
    if request.method == "POST":
        destination = request.POST['destination']
        if destination:
            data = Flight.objects.filter(destination=destination)
            return render(request, 'flight_details.html', {'flights': data})
        else:
             return redirect('flight_details')
    else:
        return redirect('flight_details')

def book_flight(request,pk):
    if request.method == "POST":
        flight = Flight.objects.get(flight_no=pk)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        nationality = request.POST['nationality']
        gender = request.POST['gender']
        dob = request.POST['dob']
        mobile = request.POST['mobile']
        address =  request.POST['address']
        passport_no =  request.POST['passport_no']
        ticket_class = request.POST['ticket_class']
        seats =  request.POST['seats']
        pay_option = request.POST['pay_option']
        name_card = request.POST['name_card']
        card_no = request.POST['card_no']
        expiration = request.POST['expiration']
        cvv = request.POST['cvv']
        pnr = str(flight.flight_no) + str(flight.destination)
        # if pay_option=="Business Class":
      
        # amount = request.POST['amount']
        passenger = Passenger(pnr=pnr, first_name=first_name, last_name=last_name, nationality=nationality,
                              flight_no=flight, gender=gender, dob=dob, mobile=mobile, address=address, passport_no=passport_no,  ticket_class= ticket_class, seats=seats, pay_option=pay_option, 
                              name_card=name_card, card_no=card_no, expiration=expiration, cvv=cvv )
        passenger.save()
        passenger.pnr = str(flight.flight_no) + str(flight.destination_code) + str(passenger.pk)
        if ticket_class == str('Business Class'):
          passenger.amount = 2900 *int(seats)
        elif ticket_class == str('Economy Class'):
            passenger.amount = 600 *int(seats)
        elif ticket_class == str('First Class'):
            passenger.amount = 3500 *int(seats)
        passenger.save()
        flight.no_of_seats -= int(seats)
        flight.save()
    #     return redirect('passenger_details', pk=passenger.pk)
    # else:
    return render(request, 'book_flight.html', {'flight_no': pk})

# def self_check_in(request,pk):
#         passenger =Passenger.object.get(Passenger, pk=pk)
#         passenger.checked_in_status = True
#         passenger.save()
#         return redirect('passenger_details', pk=passenger.pk)    


def create_pdf(request, pk):
    passenger = get_object_or_404(Passenger, pk=pk)
    html = loader.render_to_string('passenger_details.html', {'passenger': passenger})
    output = pdfkit.from_string(html, output_path=False)
    response = HttpResponse(content_type="application/pdf")
    response.write(output)
    return response   

# def staff_home(request, flight_no):
#     # staff = get_object_or_404(Staff, pk=pk)
#     data = Passenger.objects.filter(flight_no=flight_no)
#     return render(request, 'staff_home.html', {'passengers': data, 'flight_no': flight_no})

# def generate_report(request, flight_no):
#     passengers = Passenger.objects.filter(flight_no=flight_no)
#     html = loader.render_to_string('staff_home.html', {'passengers': passengers, 'flight_no': flight_no})
#     output = pdfkit.from_string(html, output_path=False)
#     response = HttpResponse(content_type="application/pdf")
#     response.write(output)
#     return response

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
        # A backend authenticated the credentials
            return redirect('/')
        else:
            return render(request, 'login.html')
    # No backend authenticated the credentials

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/')