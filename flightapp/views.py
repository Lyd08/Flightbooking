from django.shortcuts import render
from .models import TodoListItem 
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login')
def todoappView(request):
    user_email = request.user.email
    all_todo_items = TodoListItem.objects.filter(user=user_email)
    return render(request, 'booking.html',  {'all_items':all_todo_items})

@login_required(login_url='/login')
def addFromView(request):
    # x = request.POST.get('todotext')
    user_email = request.user.email
    new_from = TodoListItem()
    new_from.user = user_email
    new_from.content = request.POST.get('content')
    new_from.save()
    return HttpResponseRedirect('/todo/') 

@login_required(login_url='/login')
def addToView(request):
    # x = request.POST.get('todotext')
    user_email = request.user.email
    new_to = TodoListItem()
    new_to.user = user_email
    new_to.to= request.POST.get('to')
    new_to.save()
    return HttpResponseRedirect('/todo/') 

@login_required(login_url='/login')
def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todo/') 

# Create your views here.
