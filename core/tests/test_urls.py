from django.test import SimpleTestCase
from django.urls import resolve, reverse
from core.views import ContactUs, Home


class TestUrls(SimpleTestCase):
    
    def test_home_page_view(self):
        url = reverse('core:home')
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_contact_us_page_(self):
        url = reverse('core:contact_us')
        self.assertEqual(resolve(url).func.view_class, ContactUs)
