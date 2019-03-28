from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
from django.http import HttpResponse
from . import forms
from .models import Task, Comment

# Create your views here.
def create_task(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            s_instance = form.save()
            s_instance.created_by =  request.user.username
            s_instance.save()
        # return render(request, 'users/post_url.html', {'e_url':e_url})
        return HttpResponse("Task Successfully created")
    else:
        form = forms.TaskForm
    return render(request, 'tasks/task_create.html', {'form':form})

def comment(request, num):
    task = Task.objects.get(id=num)
    if request.method == 'GET':
        form = forms.CommentForm()
    elif request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.user = request.user
            comment.save()
            # app.votes += 1
            # app.save()
            return HttpResponse('Comment Added')
    return render(request, 'tasks/comment.html', {'task_id':num,'form':form})

def commentreply(request, num):
    comment = Comment.objects.get(id=num)
    if request.method == 'GET':
        form = forms.CommentReplyForm()
    elif request.method == 'POST':
        form = forms.CommentReplyForm(request.POST)
        if form.is_valid():
            commentreply = form.save(commit=False)
            commentreply.comment = comment
            commentreply.user = request.user
            commentreply.save()
            # app.votes += 1
            # app.save()
            return HttpResponse(' Reply to Comment Added')
    return render(request, 'tasks/commentreply.html', {'comment_id':num,'form':form})
