from django.contrib import admin
from .models import Task, Comment, CommentReply

# Register your models here.
admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(CommentReply)
