from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.
class GrammarTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        self.url = reverse('user:logar_user')

    def test_grammar_list(self):
        self.client.login(username='john', password='johnpassword')
        response = self.client.get(reverse("grammar:grammar_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,"grammar_list.html")

