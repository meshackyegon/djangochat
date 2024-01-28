from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room, Message, Messages

@login_required
def rooms(request):
    rooms = Messages.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, user_id):
    room = Messages.objects.get(user_id=user_id)
    messages = Messages.objects.filter(message_body=user_id)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})

@login_required
def messages(request):
    messages=Messages.objects.all()
    return render(request,'room/messages.html',{'messages':messages})