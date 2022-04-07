from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=250)
    body = models.TextField()
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pages')
    date = models.DateTimeField()
    
    def __str__(self):
        return f'{self.title}'