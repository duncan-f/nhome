from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=255, null=False)
    slug        = models.SlugField(max_length=255, null=False, unique=True)
    content     = models.TextField(null=False)
    draft       = models.BooleanField()
    #readtime    = models.IntegerField()
    #published   = models.DateTimeField('Published at')
    created     = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug': self.slug})

class Comment(models.Model):
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    post        = models.ForeignKey(Post, on_delete=models.CASCADE)
    content     = models.TextField(null=False)
    created     = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.content


