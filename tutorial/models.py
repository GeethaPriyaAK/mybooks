from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    published = models.BooleanField(default=False)


class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    published = models.BooleanField(default=False)



def __str__(self):
    return self.title
