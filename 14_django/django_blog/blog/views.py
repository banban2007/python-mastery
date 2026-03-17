from django.shortcuts import render,redirect
from .models import *
from  django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required,permission_required
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def search_by(request):
    search = request.GET.get('searchbox')
    posts = PostModel.objects.all()
    if search:
        posts = PostModel.objects.filter (
            Q(title__icontains=search) |
            Q(body__icontains=search)
            )
    categories = CategoryModel.objects.all()
    return render(request,'postList.html',{"posts":posts,"categories":categories})

def filter_by(request,cid):
    posts = PostModel.objects.filter(category=cid)
    categories = CategoryModel.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'postList.html',{"posts":page_obj,"categories":categories,"cid":cid})


@permission_required('blog.add_postmodel',login_url='login')
def postCreate(request):
    if request.method == "GET":
        categories = CategoryModel.objects.all()
        return render(request,'postCreate.html',{"categories":categories})
    if request.method == "POST":
        post=PostModel.objects.create(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            image = request.FILES.get('image'),
            author_id = request.user.id,
            created_at=datetime.now()
        )
        post.save()
        post.category.set(request.POST.getlist('category'))
        messages.success(request, "The Post has Been created successfully.")
        return redirect('/blog/List/')
    
def postList(request):
    posts = PostModel.objects.all()
    categories = CategoryModel.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'postList.html',{"posts":page_obj,"categories":categories})

@permission_required('blog.view_postmodel',login_url='login')
def postDetail(request,id):
    post = PostModel.objects.get(id=id)
    comments = CommentModel.objects.filter(post_id=id)
    user = User.objects.get(id=post.author_id)
    return render(request,'postDetail.html',{"post":post,"comments":comments,"author":user})

def cmt_delete(request,cid,pid):
    comment = CommentModel.objects.get(id=cid)
    comment.delete()
    return redirect('/blog/detail/' + str(pid) +'/')

def cmtUpdate(request,cid,pid):
    comment = CommentModel.objects.get(id=cid)
    if request.method == "GET":
        return render(request,'commentUpdate.html', {"comment":comment,"post_id":pid})
    if request.method == "POST":
        comment.content = request.POST.get('content')
    comment.save()
    return redirect('/blog/detail/' + str(pid) +'/')

@permission_required('blog.change_postmodel',login_url='login')
def postUpdate(request,id):
    post = PostModel.objects.get(id=id)
    if request.method == "GET":
        categories = CategoryModel.objects.all()
        return render(request,'postUpdate.html',{"post":post,"categories":categories})
    if request.method == "POST":
        post.title=request.POST.get('title')
        post.body=request.POST.get('body')
        if request.FILES.get('image'):
            post.image.delete()
            post.image = request.FILES.get('image')
        post.save()
        post.category.set(request.POST.getlist('category'))
        messages.success(request, "The Post has Been Updated successfully.")
        return redirect('/blog/List/')
@permission_required('blog.change_postmodel',login_url='login')


@permission_required('blog.delete_postmodel',login_url='login')
def Delete(request,id):
    post =PostModel.objects.get(id=id)
    if post.image:
        post.image.delete()
    post.delete()
    messages.error(request, "The Post has Been Delete.")
    return redirect('/blog/List/')

def postLogin(request):
    if request.method == "GET":
        return render(request,'postLogin.html')
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request,"you are now logged in as "+ username)
            return redirect('/blog/List/')
        else:
            messages.error(request,"Username or Password is incoorect! ")
            return render(request, 'postLogin.html')
def Logout(request):
    logout(request)
    return redirect('/blog/List/')

def cmt_create(request,post_id):
    if request.method == "POST":
        comment = CommentModel.objects.create(
            content = request.POST.get('content'),
            author_id = request.user.id,
            post_id = post_id,
        )
        comment.save()
        messages.success(request, "The comment has been created successfully")
        return redirect('/blog/detail/' + str(post_id) +'/')