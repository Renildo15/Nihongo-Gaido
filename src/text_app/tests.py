from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import *
import datetime

# Create your tests here.
class LoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

    def testLogin(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse('testlogin-view'))
        self.assertEqual(response.status_code, 200)

class TextTests(TestCase):
    @classmethod
    def setUpTestData(cls):
       cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
       )

       cls.text = Text.objects.create(
        titulo="Titulo Teste", texto="Texto teste",comentario="comentario teste",slug="kagami-no-dengou", 
        date_created= datetime, criado_por = cls.user, 
       )

    def test_text_model(self):
        self.assertEqual(self.text.titulo, "Titulo Teste")
        self.assertEqual(self.text.texto, "Texto teste")
        self.assertEqual(self.text.comentario, "comentario teste")
        self.assertEqual(self.text.slug, "kagami-no-dengou")
        self.assertEqual(self.text.date_created, datetime.datetime.now)
        self.assertEqual(self.text.criado_por.username,"testuser")

    def test_url_exists_at_correct_location_listview(self): 
        response = self.client.get(reverse("text:text_list"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("text_view/kagami-no-dengou")
        self.assertEqual(response.status_code, 200)

    def test_text_listview(self): # new
        response = self.client.get(reverse("text:text_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lista De Textos")
        self.assertTemplateUsed(response, "text_list.html")

    def test_post_detailview(self):
        response = self.client.get(reverse("text:text_view", args=(self.text.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "text_view.html")