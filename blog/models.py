from django.db import models
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    """
        Will be used for workify Desktop app
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    cover = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    promote = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    # Showes count of likes
    def likes_count(self):
        return self.apost.count()

    # my own code :
    # def user_can_like(self):
    #     can_like = True
    #     if self.ulike.exists():
    #         can_like = False
    #     return can_like

    def user_can_like(self, user):
        user_like = user.ulike.all()
        qs = user_like.filter(post=self)
        if qs.exists():
            return True
        return False

    def __str__(self):
        return f'{self.author} wrote {self.title} at {self.created}'


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ucomment')
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='acomment')
    reply = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='rcomment')
    is_reply = models.BooleanField(default=False)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:30]}'

    class Meta:
        ordering = ('-created',)


class Like(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='alike')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ulike')

    def __str__(self):
        return f'{self.user} likes {self.article}'
