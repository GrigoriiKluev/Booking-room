
from .views import Info
from django.urls import path



app_name = 'mainapp'

urlpatterns = [
    
    path('',Info.as_view(), name='RoomInfo'),
    
    
]