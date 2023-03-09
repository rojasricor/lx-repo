from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTask, NewProject

# Create your views here.
def index(request):
    title = 'Welcome to RSystfip, now with en python created!'
    return render(request, 'index.html', {"title": title})

def about(request):
    return render(request, 'about.html', {
        "developer": 'Ricardo rojas'
    })

def projects(request):
    projects =  Project.objects.all()
    return render(request, 'projects/projects.html', {
        "projects": projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        "tasks": tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            "form": NewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
        description=request.POST['description'], project_id=3)
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            "form": NewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        "project": project,
        "tasks": tasks
    })