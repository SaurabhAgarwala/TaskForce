from django import forms
from .models import User, Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        # fields = ['name', 'users']
        exclude = ['created_by']
    
    def __init__ (self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields["users"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["users"].help_text = ""
        self.fields["users"].queryset = User.objects.all()
        
# class PostEditForm(forms.ModelForm):
#     class Meta:
#         model = models.Content
#         fields = ['body']
