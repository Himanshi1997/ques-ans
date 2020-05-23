from rest_framework import serializers

from answer.models import Answer
from question.serializers import QuesDetailSerializers
from users.serializers import UserDetailSerializers


class AnsListSerializers(serializers.ModelSerializer):

    ques_title = serializers.CharField(source='ques.title')

    class Meta:
        model = Answer
        fields = ['ques', 'ques_title', 'body', 'created_by']


class AnsDetailSerializers(serializers.ModelSerializer):
    ques_detail = QuesDetailSerializers(source='ques', fields=('title', 'body'), read_only=True)
    created_by_details = UserDetailSerializers(source='created_by', fields=('user_name', 'user_ID'), read_only=True)


    class Meta:
        model = Answer
        fields = ['id', 'body', 'ques', 'ques_detail',
                  'created_on', 'modified', 'created_by', 'created_by_details']







