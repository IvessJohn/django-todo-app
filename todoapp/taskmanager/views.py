from asyncio import tasks
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks: Task = Task.objects.all().order_by('completed')

    taskform: TaskForm = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'tasks_incomplete': tasks.filter(completed=False),
        'tasks_completed': tasks.filter(completed=True),
        'taskform': taskform,
    }
    return render(request, 'taskmanager/list.html', context)

def updateTask(request, task_id: int):
    task: Task = Task.objects.get(id=task_id)
    taskform: TaskForm = TaskForm(instance=task)

    if request.method == "POST":
        taskform = TaskForm(request.POST, instance=task)
        if taskform.is_valid:
            taskform.save()
        return redirect('/')

    context = {
        'task': task,
        'taskform': taskform,
    }
    return render(request, 'taskmanager/update.html', context)

def deleteTask(request, task_id: int):
    task: Task = Task.objects.get(id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {
        'task': task,
    }
    return render(request, 'taskmanager/delete.html', context)

def about(request):
    return render(request, 'taskmanager/about.html')