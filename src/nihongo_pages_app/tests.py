from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class PagesTests(TestCase):

    def test_pages_home(self):
        response = self.client.get(reverse("pages:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"pages/index.html")


    def test_pages_about(self):
        response = self.client.get(reverse("pages:sobre"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"pages/sobre.html")