from django.shortcuts import render
from django.http import request
from .models import Post
# Create your views here.

def index(request):
    all_post = Post.objects.all()
    return render(request,'index.html',{'all_post':all_post})

def add(request):
    return render(request,'add.html')