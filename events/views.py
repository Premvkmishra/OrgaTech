from django.shortcuts import render, redirect
from .models import Event
from django.http import HttpResponse

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def post_event(request):
    if request.method == 'POST':
        event_name = request.POST.get('name')
        address = request.POST.get('address')
        date = request.POST.get('date')
        time = request.POST.get('time')
        phone = request.POST.get('phone')
        
        event = Event(name=event_name, address=address, date=date, time=time, phone=phone)
        event.save()
        return redirect('index')
    
    return render(request, 'post_event.html')