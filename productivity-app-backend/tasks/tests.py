from django.test import TestCase
from .models import Task
from django.contrib.auth.models import User

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(title='Test Task', due_date='2025-12-01T12:00:00Z')

    def test_is_overdue(self):
        self.assertTrue(self.task.is_overdue())  # Adjust due_date to test