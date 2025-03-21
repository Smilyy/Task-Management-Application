from django.urls import path 
from . import views

app_name = 'tasks_app'

urlpatterns = [
    path('tasks/new', views.task_create, name='task_create'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.category_tasks, name='category_tasks'),
    path('test_500_error/', views.test_500_error, name='test_500_error'),
]
