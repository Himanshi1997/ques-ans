from rest_framework import serializers
from users.models import Users
from core.serializers import DynamicFieldsModelSerializer
from question.models import Question
# from question.serializers import QuesListSerializers
from rest_framework import serializers


class UserListSerializers(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id','user_name', 'user_ID']


class UserDetailSerializers(DynamicFieldsModelSerializer):
    ques_asked = serializers.SerializerMethodField(default=0)
    ques_answered = serializers.SerializerMethodField(default=0)

    def get_ques_asked(self, obj):
        q = obj.question_set.all().count()
        return q

    def get_ques_answered(self, obj):
        q = obj.answer_set.all().count()
        return q

    class Meta:
        model = Users
        fields = ['user_name', 'user_ID', 'phone_no', 'ques_asked', 'ques_answered']





