from django.test import SimpleTestCase
from ..forms import RegisterForm
from ..models import User

class TestRegisterForm(SimpleTestCase):

    def test_register_form(self):
        User.objects.create(
            email="jack@gmail.com",
            password="jackpass1384",
        )
        form = RegisterForm(data={
            "email":"jack@gmail.com",
            'password':"jackpass1384",
        })

        self.assertEqual(len(form.is_valid()), 1)