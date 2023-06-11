from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .serializers import TodosSerializer
from .models import Todos

# Create your views here.

class TodosListView(generics.ListCreateAPIView):
    model = Todos
    serializer_class = TodosSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        return Todos.objects.all()
    
class SingleTodoView(generics.RetrieveUpdateAPIView):
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def delete(self, request, pk):
        drinks = Todos.objects.filter(id=pk)
        drinks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)