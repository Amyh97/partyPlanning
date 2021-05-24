from django.shortcuts import render
from .models import task


def index(request):
    """ a view to return index page """

    tasks = task.objects.filter(complete=False)

    context = {
        'tasks': tasks,
    }
    return render(request, 'home/index.html', context)
