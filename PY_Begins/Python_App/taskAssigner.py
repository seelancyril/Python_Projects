from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import login_form

def taskAssigner(request):
    form = login_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        User = authenticate(username=username, password=password)
        if User:
            login(request, User)
            print("logged IN:", request.user.is_authenticated())
            return render(request, 'Python_App/home.html')

    return render(request, 'Python_App/Task_Assigner.html', {"form":form})

def task_login(request):
    return render(request, "Python_App/Task_Assigner.html")