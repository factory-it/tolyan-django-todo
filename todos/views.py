from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import TodosSerializer
from .models import Todos

# Create your views here.

class TodosListView(generics.ListCreateAPIView):
    model = Todos
    serializer_class = TodosSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Todos.objects.all()