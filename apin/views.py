from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from task.models import Project,Task
from .serializer import ProjectSerializer,TaskSerializer
# Create your views here.
@api_view(['GET'])
def Projectdata(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many = True)
    return Response(serializer.data)
@api_view(['POST'])
def addProjectdata(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer)

@api_view(['GET'])
def Taskdata(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

def addTaskData(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer)

