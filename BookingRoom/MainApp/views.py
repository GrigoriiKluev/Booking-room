from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from MainApp.models import RoomProfile, BookingProfile
from django.views.generic import DetailView, View, TemplateView
from MainApp.forms import BookingFormer

import copy


class Info(TemplateView):
    template_name = "MainApp/roomprofile_form.html"

    def get(self, request):
        title = "Информация о комнатах"
        object_list = {
            'room': RoomProfile.get_items,
            'title': title,
        }
        return render(request, self.template_name, object_list)


class BookingDetails(DetailView):
    def get(self, request, pk):
        title = "Бронирование "
        obj = get_object_or_404(RoomProfile, pk=pk)
        if request.method == "POST":
            room_form = BookingFormer(request.POST, request.FILES)
            if room_form.is_valid():
                booking_object = BookingProfile.get_items
                booking_object.save()
                room_form.save()
                return HttpResponseRedirect(reverse("MainApp/booking-details.html"))
        else:
            room_form = BookingFormer()
        context = {
            'title': title,
            'form': room_form,
            'obj': obj,
        }
        return render(request, "MainApp/booking-details.html", context)


class UpdatedRoom(View):
    def get(self, request):
        title = "Обновленная Информация"
        BookingProfile.busy_room()
        context = {
            'title': title,
            'obj': BookingProfile.get_items,
            'room': RoomProfile.get_items
        }
        return render(request, "MainApp/updated-room-page.html", context)

    def post(self, request):
        book_form = BookingFormer(request.POST)
        if book_form.is_valid():
            book_form.save()
            return HttpResponseRedirect(reverse("updated_room_page"))

