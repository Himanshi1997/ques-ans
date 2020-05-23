from rest_framework.exceptions import ValidationError

from answer.models import Answer
from answer.serializers import AnsDetailSerializers, AnsListSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status


class AnsView(GenericAPIView):

    def get(self, request, pk=None):
        if not pk:
            ans = Answer.objects.all()
            serializer = AnsListSerializers(ans, many=True)
            return Response(serializer.data)
        else:
            return self.get_ans_detail(pk)

    def get_ans_detail(self, pk):
        ans = Answer.objects.filter(pk=pk).first()
        if ans:
            serializer = AnsDetailSerializers(ans)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = AnsDetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        ans = Answer.objects.filter(pk=pk).first()
        if ans:
            serializer = AnsDetailSerializers(ans, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)






