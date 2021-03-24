from django.test import SimpleTestCase
from django.urls import resolve, reverse
from core.views import AboutUsList, ContactUs, Home, Portfolio, ServicesView


class TestUrls(SimpleTestCase):
    
    def test_home_page_view(self):
        url = reverse('core:home')
        self.assertEqual(resolve(url).func.view_class, Home)

    def test_contact_us_page(self):
        url = reverse('core:contact_us')
        self.assertEqual(resolve(url).func.view_class, ContactUs)

    def test_about_us_page(self):
        url = reverse('core:about_us')
        self.assertEqual(resolve(url).func.view_class, AboutUsList)

    def test_services_page(self):
        url = reverse('core:services')
        self.assertEqual(resolve(url).func.view_class, ServicesView)

    def test_portfolio_page(self):
        url = reverse('core:portfolio')
        self.assertEqual(resolve(url).func.view_class, Portfolio)
