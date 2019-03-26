from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'assignee', 'created_by']

# class PostEditForm(forms.ModelForm):
#     class Meta:
#         model = models.Content
#         fields = ['body']
