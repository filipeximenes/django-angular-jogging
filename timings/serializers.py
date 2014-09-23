# coding: utf-8

from rest_framework import serializers

from timings.models import Timing


class TimingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timing
        fields = ('id', 'time', 'distance', 'date', 'user')
