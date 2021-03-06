from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from . import forms
from .models import Task, Comment
from users.models import Team

# Create your views here.

@login_required(login_url="/")
def create_task(request):
    user = request.user
    teams = user.team_set.all()
    if request.method == 'POST':
        if len(teams)==0:
            form = forms.TeamlessTaskForm(request.POST)
            if form.is_valid():
                s_instance = form.save()
                s_instance.created_by =  request.user.username
                s_instance.assignee = [user]
                s_instance.save()
                return redirect('users:userpage')
        else:
            form = forms.PostTeamForm(request.POST)
            if form.is_valid():
                team = form.cleaned_data['team']
                if team == None:
                    form = forms.TeamlessTaskForm()
                    return render(request, 'tasks/selfassigned_taskcreate.html', {'form':form})
                else:
                    team_obj = Team.objects.get(name=team)
                    form = forms.GetTeamTaskForm(team_obj.users)
                    return render(request, 'tasks/teamtask_create.html', {'form':form, 'team':team})
    else:
        if len(teams)==0:
            form = forms.TeamlessTaskForm()
            return render(request, 'tasks/task_create.html', {'form':form})
        else:
            form = forms.GetTeamForm(teams)
            return render(request, 'tasks/post_teamtask_create.html', {'form':form})

@login_required(login_url="/")
def create_selfassigned_task(request):
    if request.method == 'POST':
        form = forms.TeamlessTaskForm(request.POST)
        if form.is_valid():
            s_instance = form.save()
            s_instance.created_by =  request.user.username
            s_instance.assignee = [request.user]
            s_instance.save()
            return redirect('users:userpage')

@login_required(login_url="/")
def create_teamtask(request):
    if request.method == 'POST':
        form = forms.PostTeamTaskForm(request.POST)
        if form.is_valid():
            s_instance = form.save()
            s_instance.created_by =  request.user.username
            team = request.POST.get('team')
            team_obj = Team.objects.get(name=team)
            s_instance.team = team_obj
            s_instance.save()
        return redirect('users:userpage')

@login_required(login_url="/")
def task_display(request,id):
    task = Task.objects.get(pk=id)
    comments = task.comment_set.all()
    assignees = task.assignee.all()    
    commentform = forms.CommentForm()
    commentreplyform = forms.CommentReplyForm()
    context = {
        'user': request.user,
        'task': task,
        'assignees': assignees,
        'comments': comments,
        'commentform': commentform,
        'commentreplyform': commentreplyform
    }
    return render(request, 'tasks/task_display.html', context)

@login_required(login_url="/")
def task_edit(request, id):  
    task = Task.objects.get(pk=id)
    if task.created_by != request.user.username:
        context = {
            'message': 'You are not allowed to access this page' 
        }
        return render(request, 'message.html', context)
    user = request.user
    teams = user.team_set.all()
    if request.method == 'POST':
        if len(teams)==0:
            form = forms.TeamlessTaskForm(request.POST)
            task.delete()
            if form.is_valid():
                s_instance = form.save()
                s_instance.created_by =  request.user.username
                s_instance.assignee = [user]
                s_instance.save()
                context = {
                    'message': 'Task successfully edited.' 
                }
                return render(request, 'message.html', context)
        else:
            form = forms.EditTeamTaskForm(request.POST)
            team = task.team
            task.delete()
            if form.is_valid():
                s_instance = form.save()
                s_instance.created_by =  request.user.username
                s_instance.team = team
                s_instance.save()
                context = {
                    'message': 'Team successfully edited.' 
                }
                return render(request, 'message.html', context)
    else:
        if len(teams)==0:
            form = forms.TeamlessTaskForm(instance=task)
            return render(request, 'tasks/task_edit.html', {'form':form, 'task':task})
        else:
            form = forms.EditTeamTaskForm(instance=task)
            return render(request, 'tasks/teamtask_edit.html', {'form':form, 'task':task})

@login_required(login_url="/")
def task_delete(request, id):
    task = Task.objects.get(id=id)
    if task.created_by != request.user.username:
        context = {
            'message': 'You are not allowed to access this page' 
        }
        return render(request, 'message.html', context)
    task.delete()
    context = {
        'message': 'Task successfully deleted.' 
    }
    return render(request, 'message.html', context)

@login_required(login_url="/")
def comment(request, num):
    task = Task.objects.get(id=num)
    form = forms.CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.task = task
        comment.user = request.user
        comment.save()
        return redirect('tasks:task-disp', id=num)

@login_required(login_url="/")
def commentreply(request, num):
    comment = Comment.objects.get(id=num)
    form = forms.CommentReplyForm(request.POST)
    if form.is_valid():
        commentreply = form.save(commit=False)
        commentreply.comment = comment
        commentreply.user = request.user
        commentreply.save()
        return redirect('tasks:task-disp', id=comment.task.id)
