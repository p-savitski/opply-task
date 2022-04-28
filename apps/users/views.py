from rest_framework import permissions, generics

from apps.users.serializers import UserSerializer


class UserRegisterAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
