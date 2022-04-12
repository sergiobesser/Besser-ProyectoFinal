from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Pages(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    body = RichTextField()
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pages')
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.title}'