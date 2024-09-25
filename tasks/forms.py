from django import forms
from django.utils import timezone

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline and deadline < timezone.now():
            raise forms.ValidationError("Deadline must be in the future")
        return deadline
