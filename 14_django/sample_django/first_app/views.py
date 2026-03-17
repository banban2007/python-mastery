from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("<h2>Welcome to django!</h2>")


def hello2(request):
    return render( request, "hello.html")

def hello3(request, title):
    return render( request, 'hello2.html', {"data":title})

def hello4(request):
    number = 1
    username = "Ban Ban"
    mgmg = {"id":1, "name":"Mg Mg", "address":"Yangon"}
    languages = ["php","python", "javascript", "Java"]
    userdata = [
        {"id":1, "name":"Mg Mg", "address":"Yangon"},
        {"id":2, "name":"Ko Ko", "address":"Mandalay"}
    ]
    return render(request, 'hello3.html', {"number":number,
    "username":username, "languages":languages, "mgmg":mgmg,
    "userdata":userdata
    }) 

def hello5(request):
    return render(request, 'sample.html')