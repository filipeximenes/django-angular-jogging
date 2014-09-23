# coding: utf-8

import django_filters

from timings.models import Timing


class TimingFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(name='date', lookup_type='gte')
    end_date = django_filters.DateFilter(name='date', lookup_type='lte')

    class Meta:
        model = Timing
        fields = ['start_date', 'end_date']
        order_by = ['date']
