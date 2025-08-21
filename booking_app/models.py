from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    TYPE_CHOICES = [
        ('standart', 'Стандарт'),
        ('premium', 'Преміум'),
        ('deluxe', 'Делюкс'),
        ('grand delux', 'Гранд Делюкс'),
        ('lux', 'Люкс'),
        ('superlux', 'Суперлюкс'),
        ('grand superlux', 'Гранд Суперлюкс')
    ]

    title = models.CharField(max_length=100, verbose_name='назва номера')
    description = models.TextField( verbose_name='опис')
    price = models.IntegerField( verbose_name='ціна')
    capacity = models.IntegerField(default=2, verbose_name='місткість номера')
    image = models.ImageField(upload_to='rooms_image', verbose_name='фото номера')
    type = models.CharField(max_length=60, choices=TYPE_CHOICES, default='standart', verbose_name='клас номера')

    def __str__(self):
        return f'{self.title}-{self.type}-{self.price}₴'

    class Meta:
        ordering = ['price', 'type']
        verbose_name = "Номер"
        verbose_name_plural = "Номери"    


class Booking(models.Model):
    STATUSES = [
        ('new', 'New'),
        ("verified", 'Verified'),
        ( 'canceled', 'Canceled'),
        ('completed', 'Completed'),
    ]


    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    email = models.EmailField()
    status = models.CharField(max_length=20, choices=STATUSES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Room{self.room} from {self.check_in} to {self.check_out}'
    
    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        ordering = ['-created_at']