from django.db import models


class AboutUsModel(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    active = models.BooleanField(default=True)