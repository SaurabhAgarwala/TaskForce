from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from . import forms

# Create your views here.
def signup_view(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("User Created Successfully")
    else:
        form = UserCreationForm()
    return render(request, 'users/signup_page.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return HttpResponse("Logged In Successfully")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login_page.html', {'form':form})

def logout_view(request):
        logout(request)
        return redirect('users:new-team')

def create_team(request):
    if request.method == 'POST':
        form = forms.TeamForm(request.POST)
        members = request.POST.get('users')
        # print(type(members))
        # print(len(members))
        # print(members)
        if form.is_valid():
            s_instance = form.save()
            s_instance.created_by =  request.user.username
            # s_instance.users = members
            s_instance.save()
        # return render(request, 'users/post_url.html', {'e_url':e_url})
        return redirect('tasks:new-task')
    else:
        form = forms.TeamForm
    return render(request, 'users/team_create.html', {'form':form})
