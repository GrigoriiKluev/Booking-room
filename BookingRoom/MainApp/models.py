from django.db import models
from django.shortcuts import reverse, HttpResponseRedirect
from django.utils.timezone import now

class RoomProfile(models.Model):
	id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	room_name = models.CharField(verbose_name = "Название " , max_length = 64 , blank = True )
	seets_count = models.PositiveIntegerField(verbose_name = "Количество мест" , default = 0)
	projector = models.BooleanField(verbose_name= "Наличие проектора", default = True)
	desk = models.BooleanField(verbose_name= "Наличие доски", default = True)
	status = models.CharField(verbose_name = 'Статус', max_length =64 , blank = True)


	def __str__(self):
		return f"{self.room_name}"
	
	@staticmethod
	def get_items():
		return RoomProfile.objects.all()


class BookingProfile(models.Model):
	booking = models.ForeignKey(RoomProfile, on_delete = models.CASCADE)
	booking_time = models.TimeField(verbose_name = " Время брони c ", default = now)
	booked_time = models.TimeField(verbose_name = "Время брони до", null=True, blank = True  )
	status = models.CharField(verbose_name = 'Статус', max_length =64 , blank = True)
	
	def __str__(self):
		return f"{self.status}"	

	@staticmethod
	def busy_room():
		get_other = BookingProfile.objects.all()
		for other in get_other:
			if other.booked_time is None:
				other.status = 'Комната свободна'
				other.save()
			else:
				other.status = 'Комната занята'
				other.save()
		return get_other	
	
	@staticmethod
	def get_items():
		return BookingProfile.objects.all()