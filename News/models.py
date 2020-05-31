from django.db import models
from django.utils import timezone
# Create your models here.


class News(models.Model):
    author = models.CharField(max_length=30)
    title  = models.CharField(max_length=30)
    description = models.TextField()
    edition = models.TextField()
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.author

class SportNews(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()
    edition = models.TextField()

    def __str__(self):
        return self.author

class DataRegistro(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)

    def __str__(self):
        return self.username