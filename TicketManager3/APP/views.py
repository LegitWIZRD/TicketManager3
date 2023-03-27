from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import Ticket
# Create your views here.


def home(request):
    tickets = Ticket.objects.all()
    if request.method == 'POST':
        username = request.POST["usr"]
        password = request.POST["pswd"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "The user name or password provided is incorrect!")
            return redirect('home')
    return render(request, 'home.html', {
        'home': home,
        'tickets': tickets
    })


def admin(request):
    return redirect('admin')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')
