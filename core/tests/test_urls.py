from django.test import SimpleTestCase
from django.urls import resolve, reverse
from core.views import Home


class TestUrls(SimpleTestCase):
    
    def test_home_page_view(self):
        url = reverse('core:home')
        self.assertEqual(resolve(url).func.view_class, Home)
