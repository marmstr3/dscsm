from django.conf import settings
from django.db import models
from django.utils import timezone
from PIL import Image

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    class Meta:
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    blog_html = models.FileField(upload_to = './blog/post_html/')
    thumbnail = models.ImageField(upload_to = 'blog/images/',
                              default = 'blog/images/default_thumbnail.png'
                              )

    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    last_edited_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['published_date']

    def __str__(self):
        return self.title

