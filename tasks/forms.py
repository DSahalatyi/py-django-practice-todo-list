from django import forms
from django.utils import timezone


class TaskForm(forms.ModelForm):
    class Meta:
        fields = ("content", "deadline", "tags")
        widgets = {
            "deadline": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }

    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline < timezone.now():
            raise forms.ValidationError("Deadline must be in the future")
        return deadline