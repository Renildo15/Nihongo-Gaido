from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

class PagesTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.url = reverse('user:logar_user')
        

    def test_pages_home(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"pages/index.html")


    def test_pages_about(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("pages:sobre"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"pages/sobre.html")