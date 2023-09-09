from django.urls import path
from .views import project_list,project_tasks,create_project,create_task,single_task
urlpatterns = [
    path('',project_list,name = 'project_list'),
    path('<int:id>/Tasks',project_tasks,name = 'project_tasks'),
    path('<int:id>',single_task,name='single_task'),
    path('new_project',create_project,name = 'create_project'),
    path('<int:id>/new_task',create_task,name = 'create_task'),
]
