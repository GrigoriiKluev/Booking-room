from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from MainApp.models import RoomProfile, BookingProfile
from django.views.generic import View, TemplateView, DeleteView, CreateView
from MainApp.forms import BookingFormer
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse


class Info(TemplateView):
    template_name = "MainApp/roomprofile_form.html"

    def get(self, request):
        title = "Информация о комнатах"
        object_list = {
            'room': RoomProfile.get_items,
            'title': title,
        }
        return render(request, self.template_name, object_list)


class BookingDetails(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    title = "Бронирование "
    template_name = "MainApp/booking-details.html"
    success_url = "updated_room_page"

    def get(self, request, pk):
        obj = get_object_or_404(RoomProfile, pk=pk)
        room_form = BookingFormer(request.POST, initial={'booking':pk})

        context = {
            'title': self.title,
            'form': room_form,
            'obj': obj,
            'result': BookingProfile.get_items,
        }
        return render(request, self.template_name, context)

class UpdatedRoom(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'author'
    template_name = "MainApp/updated-room-page.html"
    model = BookingProfile
    fields = ['booking']


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
        err = HttpResponseRedirect(reverse('error'))
        update = HttpResponseRedirect(reverse('updated_room_page'))
        if book_form.is_valid() and BookingProfile.correct_time:
            data_day = book_form.cleaned_data.get('day')
            input_time_from = book_form.cleaned_data.get('booking_time')
            input_time_to = book_form.cleaned_data.get('booked_time')
            book = book_form.cleaned_data.get('booking')
            callback = BookingProfile.booking_compare(data_day, book, data_day, input_time_to, input_time_from,book_form, request, update, err)
            return callback
        else:
            return HttpResponseRedirect(reverse('error'))


class DeleteBook(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'author'
    model = BookingProfile
    template_name = "MainApp/delete_book.html"
    success_url = reverse_lazy('updated_room_page')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)


def error(request):
    title = "Обновленная Информация"
    room_form = BookingFormer()
    context = {
        'title': title,
        'form': room_form,
        'obj': RoomProfile.get_items,
        'result': BookingProfile.get_items,
    }
    return render(request, "MainApp/error.html", context)

