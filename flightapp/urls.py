from django.urls import path
from . import views

app_name = 'flightapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todoappView, name='todo'),
    path('addFromItem/',views.addFromView), 
    
    path('deleteTodoItem/<int:i>/', views.deleteTodoView), 
] 