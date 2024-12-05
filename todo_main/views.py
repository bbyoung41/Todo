from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task


def home(request):
    not_completed_tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
    completed_tasks = Task.objects.filter(is_completed = True). order_by('-updated_at')
    context = { 
        'not_completed' : not_completed_tasks,
        'completed' : completed_tasks,
    }
    
    return render(request,'home-todo.html', context)