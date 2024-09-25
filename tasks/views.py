from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from tasks.forms import TaskForm
from tasks.models import Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")
