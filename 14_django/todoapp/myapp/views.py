from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def Create(request):
    if request.method == "GET":
        return render(request,'create.html')
    if request.method == "POST":
        todo = Todo.objects.create(
            name=request.POST.get("name"),
            description=request.POST.get("description")
        )
        todo.save()
        return redirect('/myapp/')
    
def List(request):
    todos = Todo.objects.all()
    return render(request,'index.html',{"todos":todos})

def Delete(request,tid):
    todo = Todo.objects.get(id=tid)
    todo.delete()
    return redirect('/myapp/')

def Details(request,tid):
      todos = Todo.objects.get(id=tid)
      return render(request,'details.html',{"todo":todos})