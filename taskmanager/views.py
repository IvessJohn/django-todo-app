from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import *
from .forms import *
from .decorators import unauthenticated_user    

# Create your views here.

#region Authentication
@unauthenticated_user
def register_view(request):
    register_form: RegisterForm = RegisterForm()

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user: User = register_form.save()
            username: str = user.username

            messages.info(request, f"User {username} was created successfully!")

            return redirect("login")

    context = {"register_form": register_form}
    return render(request, "taskmanager/auth_register.html", context)


@unauthenticated_user
def login_view(request):
    if request.method == "POST":
        _username: str = request.POST.get("username")
        _password: str = request.POST.get("password")

        user: User = authenticate(request.POST, username=_username, password=_password)

        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            messages.info(request, "Username or password is incorrect.")

    context = {}
    return render(request, "taskmanager/auth_login.html", context)


@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return redirect("login")

#endregion

#region Main views
@login_required(login_url="login")
def index(request):
    """Main page. All the tasks are shown here."""
    tasks: Task = Task.objects.filter(owner=request.user)
    tasks = tasks.order_by("completed")  # Incomplete go first
    task_form: TaskForm = TaskForm()

    # Create a new task from the POST method
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid:
            task: Task = task_form.save()
            task.owner = request.user
            task.save()
        return redirect("/")

    context = {
        "tasks": tasks,
        "tasks_incomplete": tasks.filter(completed=False),
        "tasks_completed": tasks.filter(completed=True),
        "task_form": task_form,
    }
    return render(request, "taskmanager/list.html", context)

#endregion

#region Task-related
@login_required(login_url="login")
def updateTask(request, task_id: int):
    """A view for the task update page."""
    task: Task = Task.objects.get(id=task_id)
    task_form: TaskForm = TaskForm(instance=task)

    # Create the edited task information from the POST method
    if request.method == "POST":
        task = TaskForm(request.POST, instance=task)
        if task.is_valid:
            task.save()
        return redirect("/")

    context = {
        "task": task,
        "task_form": task_form,
    }
    return render(request, "taskmanager/update.html", context)


@login_required(login_url="login")
def deleteTask(request, task_id: int):
    """A view for the task deletion page."""
    task: Task = Task.objects.get(id=task_id)

    # Receive task deletion confirmation
    if request.method == "POST":
        task.delete()
        return redirect("/")

    context = {
        "task": task,
    }
    return render(request, "taskmanager/delete.html", context)

#endregion

def about(request):
    """A view for the About page."""
    return render(request, "taskmanager/about.html")
