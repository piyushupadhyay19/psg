from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Shipping
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# password for test user is Dhruv@07.03.2003
# Create your views here.
def index(request):
    context = {
        "variable1":"Piyush is great",
        "variable2":"Ronaldo is great"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def shop(request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")
        username = request.POST.get("username")
        email = request.POST.get("email")
        address = request.POST.get("address")
        address2 = request.POST.get("address2")
        country = request.POST.get("country")
        zip = request.POST.get("zip")
        ccName = request.POST.get("cc-name")
        ccNumber = request.POST.get("cc-number")
        ccExpiration = request.POST.get("cc-expiration")
        ccCvv = request.POST.get("cc-cvv")
        shipping = Shipping(firstName=firstName,lastName=lastName,username=username,email=email,address=address,address2=address2,country=country,zip=zip,ccName=ccName,ccNumber=ccNumber,ccExpiration=ccExpiration,ccCvv=ccCvv,date=datetime.today())
        shipping.save()
        messages.success(request, 'Congratulations! Your order has been placed.')
    return render(request, 'shop.html')


def players(request):
    return render(request, 'players.html')


def about(request):
    return render(request, 'about.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
        # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')
