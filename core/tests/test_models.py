from django.test import TestCase
from ..models import ContactUsModel
from accounts.models import User

class TestModels(TestCase):
    def setUp(self):
        user = User.objects.create(email="jack@gmail.com", password="amir1384")
        contact = ContactUsModel.objects.create(
            user=user, 
            fullname="Amir-Mohamad", 
            title="This is a title",
            description="This is description"
        )