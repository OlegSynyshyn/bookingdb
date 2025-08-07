from django.shortcuts import render
from booking_app.models import Room, Booking

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', context={'rooms': rooms})


def room_info(request, room_id ):
    rooms = Room.objects.get(id=room_id)
    return render(request, 'room-info.html', context={'room':rooms})