from django.db import models


class AboutUsModel(models.Model):
    name = models.CharField(max_length=100)