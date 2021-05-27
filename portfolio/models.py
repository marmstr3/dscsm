from django.db import models
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    preview = models.ImageField(upload_to="../demo_media/portfolio/images/",
                                default="../demo_media/portfolio/images/default_preview.png")
    last_edited_date = models.DateTimeField(default=timezone.now)
    github_url = models.CharField(max_length=200, default="")
    project_url = models.CharField(max_length=200, blank=True)


    class Meta:
        ordering = ['last_edited_date']
    
    def __str__(self):
        return self.title
