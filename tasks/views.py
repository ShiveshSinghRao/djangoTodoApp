from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

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

def updateTask(request,pk):
    return render(request,'tasks/update_task.html')