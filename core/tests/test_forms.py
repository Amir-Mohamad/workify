from django.test import SimpleTestCase
from ..forms import ContactUsForm, NewsLetterForm, OrderForm


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


class TestOrderForm(SimpleTestCase):
    def test_valid_data(self):
        form = OrderForm(data={
            'title':'title',
            'description':'description',
            'phone':'09104958451',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = OrderForm(data={})
        self.assertEqual(len(form.is_valid), 3)