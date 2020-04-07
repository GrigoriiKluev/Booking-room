from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from MainApp.models import RoomProfile, BookingProfile
from django.views.generic import DetailView, View, TemplateView,DeleteView,CreateView
from MainApp.forms import BookingFormer
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages



class Info(TemplateView):
    template_name = "MainApp/roomprofile_form.html"

    def get(self, request):
        title = "Информация о комнатах"
        object_list = {
            'room': RoomProfile.get_items,
            'title': title,
        }
        return render(request, self.template_name, object_list)

class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False
    def form_valid(self,form):
        messages.success(self.request, self.success_msg)
        return super().form_valid(form)

class BookingDetails(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'author'

    def get(self, request, pk):
        title = "Бронирование "
        obj = get_object_or_404(RoomProfile, pk=pk)

        if request.method == "POST":
            room_form = BookingFormer(request.POST, request.FILES)
            if room_form.is_valid():

                room_form.save()

                return HttpResponseRedirect(reverse("updated_room_page"))
        else:
            room_form = BookingFormer()
        context = {
            'title': title,
            'form': room_form,
            'obj': obj,
        }
        return render(request, "MainApp/booking-details.html", context)
'''
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)
'''
class UpdatedRoom(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'author'
    template_name = "MainApp/updated-room-page.html"

    def get(self, request):
        title = "Обновленная Информация"
        BookingProfile.busy_room()
        context = {
            'title': title,
            'obj': BookingProfile.get_items,
            'room': RoomProfile.get_items
        }
        return render(request, self.template_name, context)

    def post(self, request):
        book_form = BookingFormer(request.POST)
        if book_form.is_valid():
            owner = book_form.save(commit=False)
            owner.author = request.user
            owner.save()

            return HttpResponseRedirect(reverse("updated_room_page"))

        else:
            title = "Обновленная Информация"
            room_form = BookingFormer()
            context = {
                'title': title,
                'form': room_form,
                'obj': RoomProfile.get_items,
            }
            return render(request, "MainApp/error.html", context)

class DeleteBook(LoginRequiredMixin,DeleteView):
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




