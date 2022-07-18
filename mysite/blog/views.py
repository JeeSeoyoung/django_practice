from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list(req:HttpRequest)-> HttpResponse:
    posts = [
        {'id':1, 'title':'html', 'content':'html is ...'},
        {'id':2, 'title':'cdd', 'content':'cdd is ...'},
        {'id':3, 'title':'javascript', 'content':'javascript is ...'},
        {'id':4, 'title':'python', 'content':'python is ...'},
        {'id':5, 'title':'django', 'content':'django is ...'},
    ]
    
    return HttpResponse(posts)