from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import complainForm
from .models import complain
from django.views.generic import ListView, DetailView

# Create your views here.
def complain_list(request):
    context = {'complain_list':complain.objects.all()}
    return render(request,'complain/complain_list.html',context)

def complain_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = complainForm()
        else:
            complain = complain.objects.get(pk=id)
            form = complainForm(instance=complain)
        return render(request, 'complain/complain_form.html', {'form':form})
    else:
        if id==0:
            form = complainForm(request.POST)
        else:
            complain = complain.objects.get(pk=id)
            form = complainForm(request.POST,instance=complain)
        if form.is_valid():
            form.save()
        return redirect('complain/list')

def complain_delete(request,id):
    complain = complain.objects.get(pk=id)
    complain.delete()
    return redirect('complain/list')