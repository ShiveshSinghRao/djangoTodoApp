from django.shortcuts import render,redirect
from django.utils import timezone



from .models import *
from .forms import TaskForm
def index(request):
    tasks=Task.objects.all()
    
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')
    else:
        form = TaskForm()

    context = {'tasks':tasks,'form':form}
    return render(request,'tasks/list.html',context)



def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        x = {'complete': True}
        # form = TaskForm(request.POST, instance=task)
        task.complete=True
        task.completed_at=timezone.now()
        task.save()
        
        return redirect('/')
        
    else:
        form = TaskForm(instance=task)
    
    context = {'tasks':task,'form':form}
    return render(request,'tasks/list.html',context)

