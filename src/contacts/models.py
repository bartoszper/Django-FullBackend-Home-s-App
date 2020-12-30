from django.db import models

# Create your models here.
class Contact(models.Model):
    listing = models.CharField(max_length=200)