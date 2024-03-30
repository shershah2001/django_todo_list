from django.shortcuts import render,redirect
from todolist.models import Task
def home(request):
    task = Task.objects.all()
    return render(request,'index.html',{
    "task":task
    })

def add_task(request):
    if request.method=='POST':
        task_title = request.POST.get('task_title')
        task_description = request.POST.get('task_description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        completed = False
        if task_title != '' and task_description !='' and due_date != '' and due_time != '':
           task = Task(
                 task_title=task_title,
                 task_description=task_description,
                 due_date=due_date,
                 due_time=due_time
                 )
           task.save()
           return redirect('home')
    else:
        return render(request,'add_task.html')
    return render(request,'add_task.html')

def completed_task (request):
    task = Task.objects.filter(completed=True)
    data={
        'task':task
    }
    return render(request,'completed.html',data)

def deleted_task(request,task_id):
    task = Task.objects.get(id=task_id)
    data={
        "task":task
    }
    return render(request,'delete.html',data)

def  remaining_task(request):
    task = Task.objects.filter(completed=False)
    data={
        "task":task
    }
    
    return render(request,'remaining.html',data)

def task_detail(request,task_id):
    task = Task.objects.get(id=task_id)
    data={
        'task':task
    }
    return render(request,'task_detail.html',data)  

def remove_task(request,task_id):
    task = Task.objects.get(id = task_id)
    if task:
        task.delete()
    return redirect('home')

def toggle_completed(request,task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('home')


