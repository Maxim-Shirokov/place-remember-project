from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from .models import UserLocation
# Create your tests here.


class PlaceListView(TestCase):
    def setUp(self):
        self.auth_client1 = Client()
        self.user1 = User.objects.create_user('test_user1', password='test_user1')
        self.auth_client1.login(username='test_user1', password='test_user1')

        self.auth_client2 = Client()
        self.user2 = User.objects.create_user('test_user2', password='test_user2')
        self.auth_client2.login(username='test_user2', password='test_user2')

        self.locate1 = UserLocation.objects.create(lat=1, long=1, user=self.user1, name='1')
        self.locate2 = UserLocation.objects.create(lat=1, long=1, user=self.user2, name='1')
        self.locate3 = UserLocation.objects.create(lat=2, long=2, user=self.user2, name='2')

    def test_list_added_place(self):
        resp1 = self.auth_client1.get(reverse('home'))
        resp2 = self.auth_client2.get(reverse('home'))

        for locate in resp1.context['userlocation_list']:
            self.assertEqual(locate.user, resp1.context['user'])

        for locate in resp2.context['userlocation_list']:
            self.assertEqual(locate.user, resp2.context['user'])

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('home'))
        self.assertTrue(resp.url.startswith('/login/?next=/'))


class AddPlaceView(TestCase):
    def setUp(self):
        self.auth_client = Client()
        self.user = User.objects.create_user('test_user_auth', password='test_user_auth')
        self.auth_client.login(username='test_user_auth', password='test_user_auth')

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get(reverse('add-place'))
        self.assertTrue(resp.url.startswith('/login/?next=/'))

        resp = self.client.post(reverse('add-place'), {})
        self.assertTrue(resp.url.startswith('/login/?next=/'))

    def test_form_valid_add_place(self):
        response = self.auth_client.post(reverse('add-place'), {'name': 'a', 'lat': 1, 'lng': 1})
        self.assertRedirects(response, reverse('home'), status_code=302,
                             target_status_code=200, fetch_redirect_response=True)

        response = self.auth_client.post(reverse('add-place'),
                                         {'name': 'a', 'lat': 1, 'lng': 1, 'comment': 'aa'})
        self.assertRedirects(response, reverse('home'), status_code=302,
                             target_status_code=200, fetch_redirect_response=True)

    def test_form_invalid_add_place(self):
        response = self.auth_client.post(reverse('add-place'), {})  # blank data dictionary
        self.assertFormError(response, 'form', 'name', 'This field is required.')

        response = self.auth_client.post(reverse('add-place'), {'name': 'a'})
        self.assertFormError(response, 'form', 'lat', 'This field is required.')
        self.assertFormError(response, 'form', 'lng', 'This field is required.')

