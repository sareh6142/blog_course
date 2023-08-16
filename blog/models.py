from django.db import models
from django.shortcuts import redirect, reverse

# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        ('pub','published'),
        ('drf','draft')
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_page', args=[self.id])

