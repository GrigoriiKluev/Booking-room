from django.conf.urls import url
from .views import Info
from django.urls import path




urlpatterns = [
    
    path('',Info.as_view(), name='RoomInfo'),
    
    
]