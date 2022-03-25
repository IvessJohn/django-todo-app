from asyncio import tasks
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    """Main page. All the tasks are shown here."""
    tasks: Task = Task.objects.all().order_by("completed")  # Incomplete go first
    task_form: TaskForm = TaskForm()

    # Create a new task from the POST method
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid:
            task_form.save()
        return redirect("/")

    context = {
        "tasks": tasks,
        "tasks_incomplete": tasks.filter(completed=False),
        "tasks_completed": tasks.filter(completed=True),
        "task_form": task_form,
    }
    return render(request, "taskmanager/list.html", context)


def updateTask(request, task_id: int):
    """A view for the task update page."""
    task: Task = Task.objects.get(id=task_id)
    task_form: TaskForm = TaskForm(instance=task)

    # Create the edited task information from the POST method
    if request.method == "POST":
        taskform = TaskForm(request.POST, instance=task)
        if task_form.is_valid:
            task_form.save()
        return redirect("/")

    context = {
        "task": task,
        "task_form": task_form,
    }
    return render(request, "taskmanager/update.html", context)


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


def about(request):
    """A view for the About page."""
    return render(request, "taskmanager/about.html")
