from rest_framework import serializers

from core.serializers import DynamicFieldsModelSerializer
from question.models import Question
from users.serializers import UserDetailSerializers


class QuesListSerializers(serializers.ModelSerializer):
    count_of_ans = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'title', 'created_on', 'created_by', 'count_of_ans']

    def get_count_of_ans(self, obj):
        return obj.answer_set.all().count()


class QuesDetailSerializers(DynamicFieldsModelSerializer):

    count_of_ans = serializers.SerializerMethodField()
    created_by_details = UserDetailSerializers(source='created_by', fields=('user_name', 'user_ID'), read_only=True)

    def get_count_of_ans(self, obj):
        return obj.answer_set.all().count()

    class Meta:
        model = Question
        fields = ['id', 'title', 'body', 'created_on',
                  'created_by', 'created_by_details',
                  'modified', 'count_of_ans']






