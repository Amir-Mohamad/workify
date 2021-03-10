from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User


class UserRegisterTest(TestCase):
    
    def setUp(self):
        client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')