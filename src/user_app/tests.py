from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'
        }
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post("login/", self.credentials, follow=True)
        print(response)

