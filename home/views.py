from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
import json
# Create your views here.
def index(request):
    cards = House.objects.all()
    return render(request,"index.html",{'cards':cards})

def contactdealer(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        customer = Customer()
    return render(request,"contactdealer.html")


def signup(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass1']
        if pass1 == pass2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,"This username already exists.")
                return render(request,"signup.html")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This email is already in use.")
                return render(request,"signup.html")
            else:
                # old code
                user = User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=pass1)
                user.save()
                print("user created")
                return redirect("login")
        else:
            messages.info(request,"Passwords are not matching.")
            redirect("signup.html")
    else:
        return render(request,"signup.html")

def login(request):
    
    if request.method == "POST":
        print("hello")
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username=username,password=pass1)
        print("user Manas Jayaswal")
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")

    else:
        return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

# def search(request):
#     searchCards = House.objects.filter(city__icontains=request.GET['searchCity'])
#     return render(request,"search.html",{'searchCards':searchCards})
#     # return HttpResponse("hello this is searchpage")

def search(request):
    cities=City.objects.values_list('city_name', flat=True)
    if(request.GET['searchCity'] in cities):
        searchCity = City.objects.get(city_name__icontains=request.GET['searchCity'])
        locs = Location.objects.filter(city_id = searchCity.city_id)
        searchCards = House.objects.filter(city = searchCity.city_id)
        return render(request,"search.html",{'searchCards':searchCards,'locs':locs})
    else:
        return HttpResponse("hello this is searchpage")


def search2(request):
    if request.GET['locSearch'] == "Select the location":   #May be removed
        searchLoc = Location.objects.all()
        print(123)
        print(searchLoc)
        return HttpResponse("you have searched")
    searchLoc = Location.objects.get(loc_name__icontains = request.GET['locSearch'])
    # print(type(searchLoc))
    # print(123)
    # print(type(searchLoc.city_id))
    city = City.objects.get(city_id = searchLoc.city_id.city_id)     #two times city id foreign key ka chakkar
    # print((city.city_name))
    searchLocCards = House.objects.filter(location = searchLoc.loc_id)
    locs = Location.objects.filter(city_id = city.city_id)
    return render(request,"search2.html",{'searchLocCards':searchLocCards,'locs':locs})


def dealerinfo(request):
    selectedDealer = Dealer.objects.get(house_id = request.GET['houseid'])
    return render(request,"dealer.html",{'selectedDealer':selectedDealer})









# if (City.objects.filter(city_name = request.GET['searchCity']) is None):
#        return HttpResponse("hello this is searchpage")
#     else:

#         cid = City.objects.filter(city_name = request.GET['searchCity'])
#         searchCards = House.objects.filter(city_id = cid)
#         return render(request,"search.html",{'searchCards':searchCards})

#     # # 
#     # cid=City.objects.get(city_name='varanasi').city_id
#     # # 
#     # if cid is not None:
#     #     return render(request,"search.html",{'searchCards':searchCards})
#     # else:
#     #     return HttpResponse("hello this is searchpage")
