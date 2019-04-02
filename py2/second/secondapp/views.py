from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from  django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def first(request):
    form=ListForm
    if request.method == 'POST' :
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items=List.objects.all
            return render(request,'first.html',{'all_items':all_items})
    else:
        all_items = List.objects.all
        return render(request,'first.html',{'all_items':all_items})

def edit(request,List_id):
    if request.method == 'POST':
        items = List.objects.get(pk=List_id)
        form = ListForm(request.POST or None,instance=items)
        if form.is_valid():
            form.save()
            all_items=List.objects.all
            return render(request,'first.html',{'all_items':all_items})
    else:
        items = List.objects.get(pk=List_id)
        return render(request,'edit.html',{'items' :items})

def delete(request,List_id):
    items=List.objects.get(pk=List_id)
    items.delete()
    return redirect('first')


def crossoff(request,List_id):
    items=List.objects.get(pk=List_id)
    items.completed=True
    items.save()
    return redirect('first')


def uncrossoff(request,List_id):
    items=List.objects.get(pk=List_id)
    items.completed=False
    items.save()
    return redirect('first')
