from django.http import HttpRequest,HttpResponse
from django.shortcuts import render
from . import models

# Create your views here.
def post_list(req:HttpRequest)-> HttpResponse:
    posts = models.Post.objects.all()
    return render(req, 'blog/post_list.html', {'post_list':posts})

def  post_detail(req: HttpRequest, pk: int) -> HttpResponse:
    post = models.Post.objects.get(pk=pk)
    return render(req, 'blog/post_detail.html', {'post':post})
    