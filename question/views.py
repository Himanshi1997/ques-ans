from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from question.filter import QuesFilter
from question.models import Question
from question.serializers import QuesDetailSerializers, QuesListSerializers


class QuesView(GenericAPIView):

    filter_backends = [DjangoFilterBackend]
    filter_class = QuesFilter

    def get(self, request, pk=None):
        if not pk:
            ques = Question.objects.all()
            qs = self.filter_queryset(ques)
            serializer = QuesListSerializers(qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return self.get_ques_detail(pk)

    def get_ques_detail(self, pk):
        ques = Question.objects.filter(pk=pk).first()
        if ques:
            serializer = QuesDetailSerializers(ques)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = QuesDetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def put(self, request, pk):
        ans = Question.objects.filter(pk=pk).first()
        if ans:
            serializer = QuesDetailSerializers(ans, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


