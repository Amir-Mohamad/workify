from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse, resolve
from core.views import Home


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_view_response_GET(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_about_us_page_response_GET(self):
        response = self.client.get(reverse('core:about_us'))
        self.assertEqual(response.status_code, 200)

    def test_contact_us_response_GET(self):
        response = self.client.get(reverse('core:contact_us'))
        self.assertEqual(response.status_code, 302) # will redirect ro login page

    def test_order_page_GET(self):
        response = self.client.get(reverse('core:order'))
        self.assertEqual(response.status_code, 200)
    
    def test_portfolio_page_GET(self):
        
    