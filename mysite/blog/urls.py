from telnetlib import DET
from django.urls import path
from django.views.generic import ListView, DetailView
# from . import views
from . import models

app_name = 'blog'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    # path('<int:pk>/', views.post_detail, name='post_detail'),
    path('', ListView.as_view(model=models.Post), name='post_list'),
    path('<int:pk>/', DetailView.as_view(model=models.Post), name='post_detail'),
]
