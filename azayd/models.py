from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    listTitle = models.CharField(max_length=255)
    listItems = ArrayField(models.CharField(max_length=255))


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='pics')

class Career(models.Model):
    jobTitle = models.CharField(max_length=255)
    jobDesc = models.TextField(max_length=255)
    jobSalary = models.CharField(max_length=255)
    jobSkills = ArrayField(models.CharField(max_length=255))
    jobEmail = models.CharField(max_length=25)
    jobImage = models.ImageField(upload_to='pics')