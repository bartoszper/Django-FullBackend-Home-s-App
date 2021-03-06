from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/%Y/%M/%D/', blank =True)
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    # is seller of the month
    is_mvp = models.BooleanField(default=True)

    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    