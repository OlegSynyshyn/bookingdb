from django.shortcuts import render
from booking_app.models import Room, Booking

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'index.html', context={'rooms': rooms})


def room_info(request, room_id ):
    rooms = Room.objects.get(id=room_id)
    if request.method == "POST":
        email = request.POST.get("email")
        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")
        new_booking = Booking(email = email,
                              check_in = check_in,
                              check_out = check_out,
                              rooms = rooms,
                              user = request.user
                              )
        new_booking.save()
    return render(request, 'room-info.html', context={'room':rooms})