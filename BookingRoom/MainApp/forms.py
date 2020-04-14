from django import forms
from .models import RoomProfile, BookingProfile




class BookingFormer(forms.ModelForm):
	class Meta:
		model = BookingProfile
		fields = ['booking_time','booked_time','day','booking']

	def clean(self):
		cleaned_data = super(BookingFormer, self).clean()
		input_time_from = cleaned_data.get('booking_time')
		input_time_to = cleaned_data.get('booked_time')

		if input_time_to < input_time_from:
			raise forms.ValidationError('Введите корректное время брони')
		return cleaned_data
