from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import TokenPairLoginSerializer, RegisterSerializer
from rest_framework import generics

# Create your views here.


class TokenPairLoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TokenPairLoginSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = RegisterSerializer