from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import todoform
from .models import todo

def index(request):

    item_list = todo.objects.order_by("-date")
    if request.method == "POST":
        form = todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('toapp')
    form = todoform()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('toapp')
