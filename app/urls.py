from django.urls import path
from .views import create_task, task_list, delete_task

urlpatterns = [
    path('tasks/create/', create_task, name='create_task'),           
    path('tasks/<int:task_id>/delete/', delete_task, name='delete_task'),
    path('tasks/', task_list, name='task_list'),  
]

