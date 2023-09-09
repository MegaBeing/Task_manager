from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Project,Task
from .forms import Create_project,Create_Task,Edit_status

# Create your views here.

# projects List
def project_list(request):
    if request.method == "POST":
        project = Project.objects.get(id=int(request.POST['id']))
        project.delete()
    projects = Project.objects.all()
    return render(request,'task/projects.html',{
        "projects":projects
    })

# Specific tasks List of the project
def project_tasks(request,id):
    if request.method == 'POST':
        task = Task.objects.get(id = int(request.POST['id']))
        task.delete()
    project = Project.objects.get(id = id)
    task = Task.objects.filter(project = project)
    return render(request,'task/task.html',{
        "project":project,
        "tasks":task
    }) 

# Single Task
def single_task(request,id):
    task = Task.objects.get(id=id)
    project_id = task.project.id
    if request.method == 'POST':
        form = Edit_status(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'{project_id}/Tasks')
    form = Edit_status(instance=task)
    return render(request,'task/single_task.html',{
        'task':task,
        'form':form,
        'project_id':project_id,
    })
# Creation of project
def create_project(request):
    if request.method == 'POST':
        form = Create_project(request.POST)
        if form.is_valid():
            form.save()
            return redirect(project_list)
    form = Create_project()
    return render(request,'task/forms.html',{
        'form':form,
    })

# Creation of Task
def create_task(request,id):
    project = Project.objects.get(id = id)
    if request.method == 'POST':
        form = Create_Task(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.project = project
            form.save()
            return redirect(project_tasks, id = id)
    form = Create_Task()
    return render(request,'task/forms.html',{
        'form':form,
    })