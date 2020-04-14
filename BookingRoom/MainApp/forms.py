from django import forms
from .models import BookingProfile
import datetime


class BookingFormer(forms.ModelForm):
    class Meta:
        model = BookingProfile
        fields = ['booking_time', 'booked_time', 'day', 'booking']
        input_formats = ['%d/%m/%Y']
        widgets = {
            'day': forms.DateInput()
        }

    def clean(self):
        cleaned_data = super(BookingFormer, self).clean()
        input_time_from = cleaned_data.get('booking_time')
        input_time_to = cleaned_data.get('booked_time')
        day = cleaned_data.get('day')

        if input_time_to < input_time_from:
            raise forms.ValidationError('Введите корректное время брони')
        elif input_time_from < datetime.datetime.now().time() and day == datetime.date.today():
            raise forms.ValidationError('Не возможно забронировать на это время')
        elif day < datetime.date.today():
            raise forms.ValidationError('Не возможно забронировать на это время')
        else:
            return cleaned_data

