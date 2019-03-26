from django import forms
from . import models

class TeamForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = ['name', 'users']

# class PostEditForm(forms.ModelForm):
#     class Meta:
#         model = models.Content
#         fields = ['body']
