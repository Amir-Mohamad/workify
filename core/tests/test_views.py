from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse, resolve
from core.views import Home


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_view_response(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)