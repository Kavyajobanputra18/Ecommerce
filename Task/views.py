from django.shortcuts import render
from django.views.generic.edit import CreateView
#from django.views.generic.edit import ListView
from django.views.generic.edit import DeleteView,UpdateView
from django.views.generic import DetailView

from .models import Task

# Create your views here.
class CreateTask(CreateView):
    model = Task
    fields = ['task_name', 'task_description']
    template_name = 'Task/create_task.html'
    success_url = '/task/view/'

"""class ViewTask(ListView):
    model = Task
    fields = ['task_name', 'task_description']
    template_name = 'Task/view_task.html'
    success_url = '/task/view/'"""

class DeleteTask(DeleteView):
    model = Task
    success_url = 'Task/view/'
    
def index(request):
    return render(request, 'Task/index.html')

class UpdateTask(UpdateView):
    model = Task
    fields = ['task_name', 'task_description']
    template_name = 'Task/update_task.html'
    success_url = '/task/view/'

class TaskDetail(DetailView):
    model = Task
    template_name = 'Task/task_detail.html'