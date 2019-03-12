from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse

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
    if request.method == 'POST':
        logout(request)
        return HttpResponse("Logged Out Successfully")