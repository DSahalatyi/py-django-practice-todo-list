from django import forms
from django.utils import timezone
from django_select2.forms import Select2MultipleWidget

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "tags": Select2MultipleWidget(attrs={"style": "width: 100%;"}),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline and deadline < timezone.now():
            raise forms.ValidationError("Deadline must be in the future")
        return deadline
