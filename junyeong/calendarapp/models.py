from django.db import models

class Schedule(models.Model):

    date = models.DateField()
    title = models.CharField(default='', max_length=30)
    content = models.TextField()