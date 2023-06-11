from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodosListView.as_view(), name="todos-list"),
  ]
