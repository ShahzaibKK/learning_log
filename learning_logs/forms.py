from django import forms
from .models import Topic


class NewTopic(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["text"]
        lebels = {"text": ""}
