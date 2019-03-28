from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'deadline', 'status']
        widgets = {
            'deadline': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }

class GetTeamForm(forms.ModelForm):
    def __init__(self, teams, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['team'].queryset = teams

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = models.Task
        fields = ['team']

class PostTeamForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['team']
        
class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['title'].label = "Title"
        self.fields['content'].label = "Comment"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = models.Comment
        fields = [
            'title',
            'content'
        ]


class CommentReplyForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = "Comment"

    def clean(self):
        return self.cleaned_data

    class Meta:
        model = models.CommentReply
        fields = [
            'content'
        ]
# class PostEditForm(forms.ModelForm):
#     class Meta:
#         model = models.Content
#         fields = ['body']
