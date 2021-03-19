from django.test import TestCase
from django.test.client import Client
from django.urls import reverse, resolve
from ..views import UserLogin, UserRegister


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    # testing status codes
    def test_login_page_GET(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
    
    def test_register_page_GET(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)

    # Testing views
    def test_login_view(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class, UserLogin)

    def test_register_view(self):
        url = reverse('accounts:register')
        self.assertEqual(resolve(url).func, UserRegister)
