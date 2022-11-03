from django.db import models
import datetime
from django.utils import timezone
from enum import unique
from unittest.util import _MAX_LENGTH


# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey('Topic', on_delete=models.PROTECT)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey('Webpage', on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
