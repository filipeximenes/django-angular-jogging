# coding: utf-8

from rest_framework import serializers

from timings.models import Timing


class TimingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timing
        fields = ('id', 'time', 'distance', 'date', 'user')


class TimingUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timing
        fields = ('id', 'time', 'distance', 'date')
