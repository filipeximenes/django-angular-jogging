# coding: utf-8

from rest_framework import serializers

from timings.models import Timings


class TimingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timings
        fields = ('id', 'time', 'distance', 'date', 'user')
