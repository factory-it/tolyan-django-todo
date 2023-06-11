from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserProfileSerializer

# Create your views here.

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = self.serializer_class(request.user, context={'request': request})

        return Response(serializer.data)