from django.db import models
from django.shortcuts import reverse, HttpResponseRedirect
from django.utils.timezone import now
from AuthApp.models import BookUser
from datetime import date


class RoomProfile(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    room_name = models.CharField(verbose_name="Название ", max_length=64, blank=True)
    img_path = models.ImageField(upload_to='pict')
    seets_count = models.PositiveIntegerField(verbose_name="Количество мест", default=0)
    projector = models.BooleanField(verbose_name="Наличие проектора", default=True)
    desk = models.BooleanField(verbose_name="Наличие доски", default=True)
    condition = models.BooleanField(verbose_name="Наличие Кондиционера", default=True)

    def __str__(self):
        return f"{self.room_name}"

    @staticmethod
    def get_items():
        return RoomProfile.objects.all()


class BookingProfile(models.Model):
    author = models.ForeignKey(BookUser, on_delete=models.CASCADE, verbose_name='Owner', blank=True, null=True)
    booking = models.ForeignKey(RoomProfile, on_delete=models.CASCADE)
    day = models.DateField(verbose_name="Дата", default=date.today)
    booking_time = models.TimeField(verbose_name=" Время брони c ", default=now)
    booked_time = models.TimeField(verbose_name="Время брони до", null=True, blank=True)
    status = models.CharField(verbose_name='Статус', max_length=64, blank=True)

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

    @staticmethod
    def delete_item():
        return BookingProfile.objects.filter(id=id).delete()

    @staticmethod
    def correct_time():
        item = BookingProfile.objects.all()
        for t in item:
            if time_in_range(t.booking_time, t.booked_time, t.booking_time):
                raise Exception
            if time_in_range(t.booking_time, t.booked_time, t.booking_time):
                raise Exception
            else:
                return True

    @staticmethod
    def booking_compare(day, book, data_day, input_time_to, input_time_from, book_form, request, update):
        book_query = BookingProfile.objects.filter(day=day, booking=book)
        for item in book_query:
            if item.day == data_day and item.booking_time <= input_time_from <= item.booked_time \
                    and item.booking_time >= input_time_to <= item.booked_time:
                return HttpResponseRedirect(reverse("error"))
            elif item.day == data_day and item.booking_time >= input_time_from <= item.booking_time and \
                    item.booking_time <= input_time_to <= item.booked_time:
                return HttpResponseRedirect(reverse("error"))
            elif item.day == data_day and item.booked_time >= input_time_from >= item.booking_time and \
                    input_time_to <= item.booked_time:
                return HttpResponseRedirect(reverse("error"))
            elif item.day == data_day and input_time_from <= item.booking_time and \
                    input_time_to >= item.booked_time:
                return HttpResponseRedirect(reverse("error"))
            elif item.day == data_day and item.booked_time >= input_time_from >= item.booking_time and \
                    item.booking_time <= input_time_to >= item.booked_time:
                return HttpResponseRedirect(reverse("error"))
        else:
            owner = book_form.save(commit=False)
            owner.author = request.user
            owner.save()

            return update


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end
