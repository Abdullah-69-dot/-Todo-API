from django.test import TestCase
from .models import Todoitem
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND 
# Create your tests here.
from rest_framework.test import APIClient

class TodoitemModelTest(APIClient):
    @classmethod
    def setUp(cls):
        cls.todo = Todoitem.objects.create(
            title="Test Todo",
            body="This is a test todo item.",
            completed = False
        )
    def test_todo(self):
        self.assertEqual(str(self.todo.title), "Test Todo")
        self.assertEqual(self.todo.body, "This is a test todo item.")
        self.assertEqual(self.todo.completed, False)
    def test_api_detailview(self):
        response = self.client.get(reverse("todo-detail", kwargs={"pk":self.todo.id}))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["title"], self.todo.title)
    def test_api_updateview(self):
        response = self.client.put(
            reverse("todo-update", kwargs={"pk":self.todo.id}),
            {
                "title":"Updated Test Todo",
                "body":"This is an updated test todo item.",
                "completed": True
            },
            format="json"
        )
        
        self.assertIn(response.status_code, [i for i in range(200,205)])
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, "Updated Test Todo")
        self.assertEqual(self.todo.body, "This is an updated test todo item.")
        self.assertEqual(self.todo.completed, True)
    def test_api_deleteview(self):
        response = self.client.delete(
            reverse("todo-delete", kwargs={"pk":self.todo.id})
        )
        self.assertIn(response.status_code, [i for i in range(200,205)])
        response = self.client.get(
            reverse("todo-detail", kwargs={"pk":self.todo.id})
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
    def test_api_listview(self):
        response = self.client.get(reverse("todo-list"))
        self.assertIn(response.status_code, [i for i in range(200,205)])
        self.assertEqual(len(response.data), 1)
    def test_api_createview(self):
        response = self.client.post(
            reverse("todo-create"),
            {
                "title":"New Test Todo",
                "body":"This is a new test todo item.",
                "completed": False
            },
            format="json"
        )
        self.assertIn(response.status_code, [i for i in range(200,205)])
        self.assertEqual(Todoitem.objects.count(), 2)
        new_todo = Todoitem.objects.get(id=response.data["id"])
        self.assertEqual(new_todo.title, "New Test Todo")
        self.assertEqual(new_todo.body, "This is a new test todo item.")
        self.assertEqual(new_todo.completed, False)