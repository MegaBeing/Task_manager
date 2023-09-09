from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    client = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(blank=True)

class Task(models.Model):
    todo = 'T'
    wip = 'W'
    onhold = 'O'
    done = 'D'
    choices = [
        (todo,"Todo"),
        (wip,"WIP"),
        (onhold,"ON-HOLD"),
        (done,"Done")
    ]
    name = models.CharField(max_length=50)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=choices,default=todo)

    
    