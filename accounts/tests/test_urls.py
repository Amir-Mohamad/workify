from django.http import response
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse, resolve
from ..views import UserLogin


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

    def test_login_view(self):
        url = reverse('accounts:login')
        self.assertEqual(resolve(url).func.view_class, UserLogin)