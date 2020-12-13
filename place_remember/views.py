from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView
from .models import UserLocation
from django.utils.decorators import method_decorator


# Create your views here.
def login(request):
    return render(request, 'place_remember/login.html')


@method_decorator(login_required, name='dispatch')
class PlaceListView(ListView):
    model = UserLocation
    template_name = 'place_remember/home.html'

    def get_queryset(self):
        return UserLocation.objects.filter(user=self.request.user)
