from django.db import models


class AboutUsModel(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    image = models.ImageField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title