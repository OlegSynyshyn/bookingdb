# urls.py
from django.urls import path
from booking_app.views import home

urlpatterns = [
    path('', home, name='home')
]