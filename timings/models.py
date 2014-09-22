# coding: utf-8

from django.db import models
from django.conf import settings


class Timings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    time = models.TimeField()
    distance = models.DecimalField(max_digits=5, decimal_places=0)
    date = models.DateField()
