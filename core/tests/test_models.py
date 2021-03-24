from django.test import TestCase
from ..models import ContactUsModel, WorkSamples
from accounts.models import User

class TestContactModels(TestCase):
    def setUp(self):
        user = User.objects.create(email="jack@gmail.com", password="amir1384")
        self.contact = ContactUsModel.objects.create(
            user=user, 
            fullname="Amir-Mohamad", 
            title="This is a title",
            description="This is description"
        )
    
    def test_contact_model(self):
        self.assertEqual(self.contact.fullname, "Amir-Mohamad")
        self.assertEqual(self.contact.title, "This is a title")
        self.assertEqual(self.contact.description, "This is description")

class TestWorkSample(TestCase):
    def setUp(self):
        self.workSample = WorkSamples.objects.create(
            title="title",
            description="description",
            github="https://github.com/Amir-Mohamad",
            promote=True,
            is_production=False,
        )

    def test_workSampleModel(self):
        self.assertEqual(self.workSample.title, "title")