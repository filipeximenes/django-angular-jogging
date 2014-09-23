# coding: utf-8

from django.db import models
from django.conf import settings


class Timing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    time = models.IntegerField()
    distance = models.IntegerField()
    date = models.DateField()
