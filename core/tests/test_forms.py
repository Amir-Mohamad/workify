from django.test import SimpleTestCase
from ..forms import ContactUsForm, NewsLetterForm


class TestContactForm(SimpleTestCase):

    def test_valid_data(self):
        form = ContactUsForm(data={
            'fullname':"amirmohamad", 
            'title':"title", 
            'description':"description"}
        )
        self.assertTrue(form.is_valid())
    
    def test_invalid_form(self):
        form = ContactUsForm(data={})
        self.assertEqual(len(form.errors), 3)