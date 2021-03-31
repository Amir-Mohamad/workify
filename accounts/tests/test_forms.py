from django.test import TestCase
from ..forms import RegisterForm
from ..models import User


class TestRegisterForm(TestCase):

    def test_register_form_used_before(self):
        User.objects.create(
            email="jack@gmail.com",
            password="jackpass1384",
        )
        form = RegisterForm(data={
            "email":"jack@gmail.com",
            'password1':"jackpass1384",
            'password2':"jackpass1384",
        })

        # we will get False because that email was created before
        self.assertEqual(bool(form.is_valid()), False)

    def test_password_not_match(self):
        form = RegisterForm(data={
            'email':'amir@gmail.com',
            'password1':'Amirtest1897',
            'password2':'Amirtest189',
        })
        self.assertEqual(len(form.errors), 1)

    def test_email_not_valid(self):
        form = RegisterForm(data={
            'email':'abc',
            'password1':'Amirtest1897',
            'password2':'Amirtest1897',
        })
        self.assertEqual(len(form.errors), 1)