from django.urls import path, include

from place_remember import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", views.login, name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.PlaceListView.as_view(), name='home'),
]