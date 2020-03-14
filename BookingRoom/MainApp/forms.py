from django import forms
from .models import RoomProfile, BookingProfile




class BookingFormer(forms.ModelForm):
	class Meta:
		model = BookingProfile
		fields = ['booking_time', 'booked_time','booking']