from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
from accounts.manager import UserManager
# Create your models here.


class User(AbstractUser):
	username = None
	email = models.EmailField(max_length=125, unique=True)
	avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg', blank=True, null=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	# backend = 'accounts.authentication.EmailBackend'

	def thumbnail(self):
		return format_html("<img width=40 height=25 style='border-radius: 20px;' src='{}'>".format(self.avatar.url))
	thumbnail.short_description = "thumbnail"
