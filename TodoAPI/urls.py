from django.urls import path , include
from .views import TodoDetailView , TodoUpdateView , TodoDeleteView , TodoListView , TodoCreateView  
urlpatterns = [
    path("<int:pk>/",TodoDetailView.as_view() , name="todo-detail"),
    path("<int:pk>/update/",TodoUpdateView.as_view() , name="todo-update"),
    path("<int:pk>/delete/",TodoDeleteView.as_view() , name="todo-delete"),
    path("list/",TodoListView.as_view() , name="todo-list"),
    path("create/",TodoCreateView.as_view() , name="todo-create"),
]
