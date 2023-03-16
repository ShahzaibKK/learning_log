from django import forms
from .models import Topic, Entry


class NewTopic(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        lebels = {"text": ""}


class NewEntry(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]
        lebels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
