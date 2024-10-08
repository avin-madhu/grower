from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

# rooms = [
#     {'id':1, 'name': "bruh let's learn"},
#     {'id':2, 'name': "nah I'm bored"},
#     {'id':3, 'name': "Yo what's up in the hood!"},
# ]

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    # we can search a athing with just few letter from it atleast (eg: search python with only "py")
    rooms = Room.objects.filter(Q(topic__name__icontains=q) | Q(name__icontains=q) | Q(description__icontains=q))

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'baseApp/home.html',context)

def room(request, roomkey):
    room = Room.objects.get(id = roomkey)
    context = {"room": room}
    return render(request, 'baseApp/room.html', context) 

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, "baseApp/room_form.html", context)


def updateRoom(request, roomkey):
    room = Room.objects.get(id = roomkey)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'baseApp/room_form.html', context)

def deleteRoom(request, roomkey):
    room = Room.objects.get(id = roomkey)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'baseApp/delete.html', {'obj': room})









