from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from grammar_app.models import *
class PhrasesTest(TestCase):

      def setUp(self):
         self.client = Client()
         self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
         self.url = reverse('user:logar_user')
         self.id = Grammar()
         self.id.save()

         self.grammar = Grammar_Phrase.objects.create(
               frase="gramatica teste", traducao="estrutura teste", observacao="explicação teste",  grammar_id= self.id , criado_por=self.user       
         )


      def test_phrase_model(self):
         self.client.login(username="john", password="johnpassword")
         self.assertEqual(self.grammar.frase, "gramatica teste")
         self.assertEqual(self.grammar.traducao, "estrutura teste")
         self.assertEqual(self.grammar.observacao, "explicação teste")
         self.assertEqual(self.grammar.criado_por.username, "john")

      def test_url_phrase_form(self):
         self.client.login(username='john', password='johnpassword')
         response = self.client.get(reverse("phrase:add_phrase", args=(self.grammar.grammar_id.id,)))
         self.assertEqual(response.status_code, 200)
         self.assertContains(response,"frase")
         self.assertTemplateUsed(response,"phrase_form.html")

      def test_url_phrase_list(self):
         self.client.login(username='john', password='johnpassword')
         response = self.client.get(reverse("phrase:phrases_list", args=(self.grammar.grammar_id.id,)))
         self.assertEqual(response.status_code, 200)
         self.assertContains(response,"gramatica teste")
         self.assertTemplateUsed(response, "phrase_list.html")

      def test_url_phrase_view(self):
         self.client.login(username="john", password="johnpassword")
         response = self.client.get(reverse("phrase:phrase_view", args=(self.grammar.grammar_id.id,)))
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "gramatica teste")
         self.assertTemplateUsed(response, "phrase_view.html")


      def test_url_phrase_update(self):
         self.client.login(username="john", password="johnpassword")
         response = self.client.get(reverse("phrase:update_phrase", args=(self.grammar.grammar_id.id,)))
         self.assertEqual(response.status_code, 200)
         self.assertContains(response, "frase")
         self.assertTemplateUsed(response, "phrase_edit.html")