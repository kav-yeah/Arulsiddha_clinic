from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    body=models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail',args=[str(self.id)])