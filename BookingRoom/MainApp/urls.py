from django.conf.urls import url
from .views import get_info
from django.urls import path




urlpatterns = [
    
    path('', get_info, name = 'RoomInfo'),
    
    
]