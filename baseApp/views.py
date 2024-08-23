from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id':1, 'name': "bruh let's learn"},
    {'id':2, 'name': "nah I'm bored"},
    {'id':3, 'name': "Yo what's up in the hood!"},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'baseApp/home.html',context)

def room(request, roomkey):
    room = None
    for i in rooms:
        if i['id'] == int(roomkey):
            room = i
    context = {'room': room}
    return render(request, 'baseApp/room.html', context)
