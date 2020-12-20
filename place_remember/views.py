from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, FormView
from .models import UserLocation
from django.utils.decorators import method_decorator
from django.conf import settings
from .forms import PlaceForm
from django.urls import reverse_lazy, reverse
from django.core import serializers


# Create your views here.
def login(request):
    return render(request, 'place_remember/login.html')


@method_decorator(login_required, name='dispatch')
class PlaceListView(ListView):
    model = UserLocation
    template_name = 'place_remember/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MAP_KEY'] = settings.MAP_KEY
        context['added_place_json'] = serializers.serialize(
            'json', UserLocation.objects.filter(user=self.request.user.id), ensure_ascii=False,
        )
        return context

    def get_queryset(self):
        return UserLocation.objects.filter(user=self.request.user.id)


@method_decorator(login_required, name='dispatch')
class AddPlaceView(FormView):
    template_name = 'place_remember/add_place.html'
    form_class = PlaceForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MAP_KEY'] = settings.MAP_KEY
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        lat = form.cleaned_data['lat']
        lng = form.cleaned_data['lng']
        comment = form.cleaned_data['comment']
        user_location = UserLocation(name=name, lat=lat, long=lng, comment=comment, user_id=self.request.user.id)
        user_location.save()
        return HttpResponseRedirect(reverse('home'))
