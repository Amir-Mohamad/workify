from django.test import TestCase
from ..forms import RegisterForm
from ..models import User

class TestRegisterForm(TestCase):

    def test_register_form(self):
        User.objects.create(
            email="jack@gmail.com",
            password="jackpass1384",
        )
        form = RegisterForm(data={
            "email":"jack@gmail.com",
            'password':"jackpass1384",
        })

        self.assertEqual(bool(form.is_valid()), False)