from django.db import models



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
