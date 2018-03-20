from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from .forms import login_form
from .models import Task

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

def create_task(request):
    title = request.POST.get("title")
    desc = request.POST.get("description")
    priority = request.POST.get("priority")
    assigned_to = request.POST.get("assigned_to")
    assigned_on = request.POST.get("assigned_on")
    assigned_by = str(request.user)
    eta = request.POST.get("eta")
    print("request values:",title, desc, priority, assigned_to, assigned_on, eta, assigned_by)
    add_task = Task(Title = title, Desc = desc, Priority = priority,
                    Assigned_To = assigned_to, Assigned_On = assigned_on,
                    Assigned_By = assigned_by, ETA = eta
                    )
    add_task.save()
    print_this = "Hello, can you pass it?"
    return redirect("/Python_App/task")
    #return render(request, 'Python_App/Task_Assigner.html', {'print_this':print_this})

def editTask(request):
    task_id = request.GET.get("task_id")
    return redirect("/Python_App/task")

def deleteTask(request):
    task_id = request.GET.get("task_id")
    print(task_id)
    data = Task.objects.get(Task_ID=task_id)
    print(data)
    data.delete()
    return redirect("/Python_App/task")