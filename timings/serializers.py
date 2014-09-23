# coding: utf-8

from rest_framework import serializers

from timings.models import Timing
from timings.timing_conversion import (
    from_formated_to_seconds, from_seconds_to_formated)


class TimingSerializerMixin(object):

    def transform_time(self, obj, value):
        return from_seconds_to_formated(value)

    def validate_time(self, attrs, source):
        value = attrs[source]

        formated = from_formated_to_seconds(value)
        if not formated:
            raise serializers.ValidationError('Invalid inputed date')

        attrs[source] = formated

        return attrs


class TimingSerializer(TimingSerializerMixin, serializers.ModelSerializer):
    time = serializers.CharField()

    class Meta:
        model = Timing
        fields = ('id', 'time', 'distance', 'date', 'user')


class TimingUpdateSerializer(TimingSerializerMixin, serializers.ModelSerializer):
    time = serializers.CharField()

    class Meta:
        model = Timing
        fields = ('id', 'time', 'distance', 'date')
