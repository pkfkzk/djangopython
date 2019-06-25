from django.shortcuts import render, redirect
import bcrypt
from .models import *
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def create_user(request):
    errors = User.objects.regValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, key)
        return redirect("/")
    else:
        password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User.objects.create(name=request.POST['name'], username=request.POST['username'], password=password_hash.decode())
        request.session['user_id'] = user.id
        return redirect("/travels")

def travels(request):
    if 'user_id' in request.session:
        user = User.objects.get(id=request.session['user_id'])
        usertrips = Trip.objects.filter(jointrip=request.session['user_id'])
        otherusertrips = Trip.objects.exclude(jointrip=request.session['user_id'])
   

        context = {
            "user": user,
            #"all_trips": Trip.objects.all()
            "usertrips": usertrips,
            "otherusertrips": otherusertrips,
            }

        return render(request, "travels.html", context)
    else:
        return redirect("/")

def login(request):
    errors= User.objects.loginValidator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, key)
        return redirect("/")
    else:
        users = User.objects.filter(username=request.POST['login_username'])
        request.session['user_id'] = users[0].id
    return redirect("/travels")

def logout(request):
    request.session.clear()
    return redirect("/")

def addtrip(request):
    return render(request, "addtrip.html")

def create_trip(request):
    errors= Trip.objects.tripValidator(request.POST)
    user = User.objects.get(id=request.session['user_id'])
    if errors:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, key)
        return redirect("/travels/add")
    else:
        trip = Trip.objects.create(destination=request.POST['destination'], description=request.POST['description'], travelDateFrom=request.POST['travelDateFrom'], travelDateTo=request.POST['travelDateTo'], planned_By_id=request.session['user_id'] )
        user.triptogether.add(trip)
    return redirect("/travels")

def join(request, trip_id):
    trip = Trip.objects.get(id = trip_id)
    user = User.objects.get(id = request.session['user_id'])
    user.triptogether.add(trip)
    return redirect("/travels")

def destination(request,trip_id):
    trip = Trip.objects.get(id= trip_id)
    users = trip.jointrip.all().exclude(id=trip.planned_By_id)
    

    context ={
        "trip": trip,
        "users": users,
    }

    return render(request, "tripdetail.html", context)


# def destination(request):

   



    
    

    

