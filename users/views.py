from .serializers import RegisterSerializer
from rest_framework import generics
from django.contrib.auth.models import User
# Create your views here.


class RegisterViewSet(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class UpdateUserView(generics.UpdateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
