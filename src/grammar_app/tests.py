from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
# Create your tests here.
class GrammarTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.url = reverse('user:logar_user')

        self.grammar = Grammar.objects.create(
            gramatica="gramatica teste", estrutura="estrutura teste", nivel="N5",  criado_por=self.user
             
        )
    def test_grammar_model(self):
        self.client.login(username='john', password='johnpassword')
        self.assertEqual(self.grammar.gramatica, "gramatica teste")
        self.assertEqual(self.grammar.estrutura, "estrutura teste")
        self.assertEqual(self.grammar.nivel, "N5")
        self.assertEqual(self.grammar.criado_por.username,"john")

    def test_url_grammar_list(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("grammar:grammar_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "gramatica teste")
        self.assertTemplateUsed(response,"grammar_list.html")

    def test_url_add_grammar(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("grammar:add_grammar"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "grammar_form.html")

    def test_url_edit_grammar(self):
        self.client.login(username="john", password='johnpassword')
        response = self.client.get('/grammar/edit_grammar/1')
        self.assertEqual(response.status_code, 200)
