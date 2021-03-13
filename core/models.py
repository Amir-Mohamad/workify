from django.db import models
from accounts.models import User


# For adding team members
class AboutUsModel(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=200)
    github = models.CharField(max_length=500)
    image = models.ImageField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Team Memeber'
        verbose_name_plural = 'Team Memebers'

    def __str__(self):
        return self.name


class WorkSamples(models.Model):
    """
        In home page we can just have 6 worksample => So i put promote
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200) # Note => DONT change it to TextField (sth like preview)
    cover = models.ImageField()
    github = models.CharField(max_length=300, null=True, blank=True) # Github repo
    promote = models.BooleanField(default=False)
    is_production = models.BooleanField(default=False)

    class Meta:
        ordering = ('promote',)
        verbose_name = 'Work Sample'
        verbose_name_plural = 'Work Sample'

    def __str__(self):
        return self.title
        

class ContactUsModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return f'{self.user} made {self.title}'

class NewsLetterModel(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()


    def __str__(self):
        return f'{self.phone} with {self.phone}'