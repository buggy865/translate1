from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Task 

def create_task(name, description, time_required):
    try:
        task = Task.objects.create(
            name=name,
            description=description,
            time_required=time_required,
            create_time=timezone.now()
        )
        return task
    except Exception as e:
        return f"Vazifa yaratishda xato: {str(e)}"

def get_task_by_id(task_id):
    return get_object_or_404(Task, id=task_id) 

def delete_task(task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return f"Vazifa o'chirildi!: {task}"

create_task("Uy ishi qilish", "Matimatikadan misollar", "1 soat")
create_task("Kitob o'qish", "Tarix kitobini o'qish", "2 soat")

def task_list(request):
    tasks = Task.objects.all() 
    return render(request, 'task_list.html', {'tasks': tasks})

