from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from tasks.forms import TaskForm
from tasks.models import Tag, Task


class TagModelTests(TestCase):
    def test_tag_str(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(str(tag), "Test Tag")


class TaskFormTests(TestCase):
    def test_task_form_valid(self):
        form = TaskForm(
            data={
                "content": "Test task",
                "deadline": timezone.now() + timedelta(hours=1),
            }
        )
        self.assertTrue(form.is_valid())

    def test_task_form_invalid(self):
        form = TaskForm(
            data={
                "content": "Test task",
                "deadline": timezone.now() - timedelta(hours=1),
            }
        )
        self.assertFalse(form.is_valid())


class TaskViewsTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            content="Test task",
        )

    def test_task_list_post_complete_task(self):
        form_data = {
            "action": "complete",
            "task_id": self.task.id,
        }
        response = self.client.post(reverse("tasks:task-list"), data=form_data)
        self.assertRedirects(response, reverse("tasks:task-list"))
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)
