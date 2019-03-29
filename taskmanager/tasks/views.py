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
                    return render(request, 'tasks/task_create.html', {'form':form})
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

@login_required(login_url="/")
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
