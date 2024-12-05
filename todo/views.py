from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from todo.models import Task

# Create your views here.
def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        newtask = request.POST['task']
        get_task.task = newtask
        get_task.save()
        return redirect('home')
    else:
        context ={
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    delete_task = get_object_or_404(Task, pk=pk)
    delete_task.delete()
    return redirect('home')


def undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')