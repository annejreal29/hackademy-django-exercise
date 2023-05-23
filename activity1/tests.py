from django.test import TestCase
from .forms import RegisterUser
from django.urls import reverse, resolve
from .views import profile_view

# Create your tests here.

class TestProfile(TestCase):
    def test_form_is_valid(self):
        form = RegisterUser(data={
            'first_name':'Jane',
            'last_name':'Smith',
            'email': 'jane@mail.com',
            'username': 'jane123',
            'password1': 'User1234',
            'password2': 'User1234'
        })

        self.assertTrue(form.is_valid())

class TestRedirect(TestCase):
    def test_url_valid(self):
        url = reverse('profile_view')
        self.assertEquals(resolve(url).func,profile_view)