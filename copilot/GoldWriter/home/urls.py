
from django.urls import path
from django.urls import include
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('thread_status/', views.thread_status, name='thread_status'),
    
]