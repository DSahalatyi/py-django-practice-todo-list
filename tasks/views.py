from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from tasks.forms import TaskForm
from tasks.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.prefetch_related("tags")
        return queryset

    def post(self, *args, **kwargs):
        action = self.request.POST.get("action")
        task = Task.objects.get(pk=self.request.POST.get("task_id"))
        if action == "complete" and not task.is_done:
            task.is_done = True
            task.save()
        if action == "undo" and task.is_done:
            task.is_done = False
            task.save()

        return HttpResponseRedirect(reverse_lazy("tasks:task-list"))


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"


class TagCreateView(CreateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = ("name",)
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
