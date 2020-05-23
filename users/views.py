from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from users.models import Users
from users.serializers import UserDetailSerializers, UserListSerializers



class UserView(GenericAPIView):

    def get(self, request, pk=None):
        if pk:
            ques = Users.objects.filter(pk=pk).first()
            if ques:
                serializer = UserDetailSerializers(ques)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return self.get_user_list()

    def get_user_list(self):
        ques = Users.objects.all()
        serializer = UserListSerializers(ques, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserDetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



