from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import *
import datetime

# Create your tests here.

class TextTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        cls.url = reverse('user:logar_user')

        cls.text = Text.objects.create(
            titulo="Titulo Teste", texto="Texto teste",comentario="comentario teste",slug="kagami-no-dengou", 
            date_created= datetime, criado_por = cls.user, 
        )

    def test_text_model(self):
        self.client.login(username='john', password='johnpassword')
        self.assertEqual(self.text.titulo, "Titulo Teste")
        self.assertEqual(self.text.texto, "Texto teste")
        self.assertEqual(self.text.comentario, "comentario teste")
        self.assertEqual(self.text.slug, "kagami-no-dengou")
        self.assertEqual(datetime.date(2022, 12, 23), datetime.date.today())
        self.assertEqual(self.text.criado_por.username,"john")

    def test_url_exists_at_correct_location_listview(self): 
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("text:text_list"))
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get("/text/text_view/kagami-no-dengou/")
        self.assertEqual(response.status_code, 200)

    def test_text_listview(self): # new
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("text:text_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Texto teste")
        self.assertTemplateUsed(response, "text_list.html")

    def test_post_detailview(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("text:text_view", args=(self.text.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "text_view.html")