from django.test import TestCase
from ..models import AboutUsModel, ContactUsModel, NewsLetterModel, OrderModel, WorkSamples
from accounts.models import User


# ContactUsModel
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



# WorkSampleModel
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
        self.assertEqual(self.workSample.description, "description")
        self.assertEqual(self.workSample.github, "https://github.com/Amir-Mohamad")
        self.assertEqual(self.workSample.promote, True)


# NewsLetterModel
class TestNewsModel(TestCase):
    def setUp(self):
        self.news = NewsLetterModel.objects.create(
            email="jack@gmail.com",
            phone="09104958451",
        )
    
    def test_news_model(self):
        self.assertEqual(self.news.email, "jack@gmail.com")
        self.assertEqual(self.news.phone, "09104958451")

class TestOrderModel(TestCase):
    def setUp(self):
        user = User.objects.create(
            email="jack@gmail.com",
            password="amir1384",
        )
        self.order = OrderModel.objects.create(
            user=user,
            title="title",
            description="description",
            phone="09104958451"
        )

    def test_order_model(self):
        self.assertEqual(self.order.title, "title")
        self.assertEqual(self.order.description, "description")
        self.assertEqual(self.order.phone, "09104958451")


class TestAboutUsModel(TestCase):
    def setUp(self):
        self.about = AboutUsModel.objects.create(
            name="name",
            bio="bio",
            github="https://github.com/Amir-Mohamad",
            instagram="https://instagram.com/megacoders",
            is_active=True,
        )
    
    def test_about_model(self):
        self.assertEqual(self.about.name, "name")
        self.assertEqual(self.about.bio, "bio")
        self.assertEqual(self.about.github, "https://github.com/Amir-Mohamad")
        self.assertEqual(self.about.instagram, "https://instagram.com/megacoders")
        self.assertEqual(self.about.is_active, True)