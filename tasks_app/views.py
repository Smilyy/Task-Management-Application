from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Task
from .forms import TaskForm
from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse(f"Hello, world. You're at the tasks {{name}}.")

#Define the home page
def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html')

#User create new tasks
def task_create(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tasks_app:task_list")
    else:
        form = TaskForm()  
    return render(request, 'task_create.html', {'form': form})

#Display a list of all tasks
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

#Display task details
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})

#Display all categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

#Displays all tasks under a specific category
def category_tasks(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tasks = Task.objects.filter(category=category)
    return render(request, 'category_tasks.html', {'category': category, 'tasks': tasks})

#Error handling
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    return render(request, '500.html', status=500)

#Test the 500 error page
def test_500_error(request):
    raise Exception("This is a test exception for the 500 error page")
