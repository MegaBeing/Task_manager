from django import forms
from .models import Project,Task

class Create_project(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','client','end_date']

class Create_Task(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','status']

class Edit_status(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']