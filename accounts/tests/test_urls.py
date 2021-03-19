from django.test import TestCase
from django.test.client import Client


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()