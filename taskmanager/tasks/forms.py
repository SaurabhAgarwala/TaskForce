from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'description', 'team', 'assignee', 'deadline', 'status']
        widgets = {
            'deadline': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }

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
