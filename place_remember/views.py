from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView


# Create your views here.
def login(request):
    return render(request, 'place_remember/login.html')


@login_required
def PlaceListView(request):
    return render(request, 'place_remember/base.html')
