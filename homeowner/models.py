
from django.db import models
import datetime
from django.utils import timezone


class Notification(models.Model):
    email = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published', default=None)

    def __str__(self):
        return self.email

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.CharField(max_length=400)
    subject = models.CharField(max_length=400)
    message = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published', default=None)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
