from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .models import Ticket
from .forms import NewTicketForm
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


def add_ticket(request):
    form = NewTicketForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                new = form.save()
                messages.success(request, "New Ticket Was Added!")
                return redirect('home')

        return render(request, 'add.html', {
            'form': form})
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('home')


def ticket(request, pk):
    if request.user.is_authenticated:
        ticket_record = Ticket.objects.get(id=pk)
        return render(request, 'ticket.html', {
            'ticket_record': ticket_record
        })
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('home')


def edit_ticket(request, pk):
    if request.user.is_authenticated:
        ticket_record = Ticket.objects.get(id=pk)
        return render(request, 'edit.html', {
            'ticket_record': ticket_record
        })
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('home')


def delete_ticket(request, pk):
    if request.user.is_authenticated:
        deleted_ticket = Ticket.objects.get(id=pk)
        deleted_ticket.delete()
        messages.success(request, f"Ticket was deleted successfully!")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to view this page.")
        return redirect('home')


def admin(request):
    return redirect('admin')


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')
