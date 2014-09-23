# coding: utf-8

from rest_framework import serializers

from timings.models import Timing
from timings.timing_conversion import (
    from_formated_to_seconds, from_seconds_to_formated)


class TimingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timing
        fields = ('id', 'time', 'distance', 'date', 'user')


class TimingUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timing
        fields = ('id', 'time', 'distance', 'date')
