from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from vocabulary_app.models import *
# Create your tests here.

class ExampleTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        cls.url = reverse('user:logar_user')
        cls.word = Word()
        cls.word.save()

        cls.example = Example.objects.create(
            frase="frase teste", leitura="leitura teste",traducao="traducao teste",anotacao="anotacao teste", 
            palavra= cls.word, slug="slug-teste", criado_por = cls.user, 
        )

    def test_example_model(self):
        self.client.login(username='john', password='johnpassword')
        self.assertEqual(self.example.frase,"frase teste")
        self.assertEqual(self.example.leitura,"leitura teste")
        self.assertEqual(self.example.traducao, "traducao teste")
        self.assertEqual(self.example.slug, "slug-teste")
        self.assertEqual(self.example.criado_por.username, "john")

