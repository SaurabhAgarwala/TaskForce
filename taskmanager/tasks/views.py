from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
from django.http import HttpResponse
from . import forms

# Create your views here.
def create_task(request):
    if request.method == 'POST':
        form = forms.TaskForm(request.POST)
        if form.is_valid():
            s_instance = form.save(commit=False)
            s_instance.created_by =  request.user
            s_instance.save()
        # return render(request, 'users/post_url.html', {'e_url':e_url})
        return HttpResponse("Task Successfully created")
    else:
        form = forms.TaskForm
    return render(request, 'users/team_create.html', {'form':form})
