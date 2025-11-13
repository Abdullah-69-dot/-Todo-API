from django.shortcuts import render
from rest_framework.generics import UpdateAPIView , RetrieveAPIView , DestroyAPIView , ListAPIView , CreateAPIView
from .models import Todoitem
from .serializer import TodoItemSerializer 
# Create your views here.
class TodoCreateView(CreateAPIView):
    queryset = Todoitem.objects.all()
    serializer_class = TodoItemSerializer
class TodoListView(ListAPIView):
    queryset = Todoitem.objects.all()
    serializer_class = TodoItemSerializer
class TodoDetailView(RetrieveAPIView):
    queryset = Todoitem.objects.all()
    serializer_class = TodoItemSerializer
class TodoUpdateView(UpdateAPIView):
    queryset = Todoitem.objects.all()
    serializer_class = TodoItemSerializer
class TodoDeleteView(DestroyAPIView):
    queryset = Todoitem.objects.all()
    serializer_class = TodoItemSerializer