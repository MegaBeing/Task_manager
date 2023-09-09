from django.urls import path
from .views import Projectdata,addProjectdata,addTaskData,Taskdata
urlpatterns = [
    path('project_data',Projectdata),
    path('add_project_data',addProjectdata),
    path('task_data',Taskdata),
    path('add_task_data',addTaskData)
]
