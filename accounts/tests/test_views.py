from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User


class UserRegisterTest(TestCase):
    
    def setUp(self):
        client = Client()

    def test_user_register_GET(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_user_login_GET(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
    

    # NOTE: I remove this func becuase we have 2 setep authentication !! (next page will be /verify)
    # def test_user_register_POST_valid(self):
    #     response = self.client.post(reverse('accounts:register'), data={
    #         'email':'kevin@gmail.com',
    #         'password1':'kevinpass',
    #         'password2':'kevinpass'
    #     })
    #     print(response)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(User.objects.count(), 1)