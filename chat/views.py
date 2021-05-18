from django.core.checks import messages
from django.shortcuts import render,redirect,HttpResponse
from django.http import  JsonResponse
from .models import *
from django.contrib import messages
from datetime import date, datetime
# Create your views here.

def home(request):
    return render(request,'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    context = {
        'username': username,
        'room': room,
        'room_details': room_details
    }
    return render(request, 'room.html', context)

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if room == '' and username == '':
            messages.warning(request,'Field Cannot Be Empty!')
            return redirect('home')
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    custom_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    new_message = Message.objects.create(value=message,date=custom_date, user=username, room=room_id)
    new_message.save()

def getMessages(request,room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})