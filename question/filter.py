import django_filters

from question.models import Question


class QuesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = Question
        fields = ('title', 'created_by')