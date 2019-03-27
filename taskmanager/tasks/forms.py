from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'assignee', 'status']

# class PostEditForm(forms.ModelForm):
#     class Meta:
#         model = models.Content
#         fields = ['body']
