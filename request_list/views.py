from django.shortcuts import render
from request.models import Request

# Create your views here.
def request_list(request):
    list = Request.objects.all()
    context = {
        'request_list': list,
    }
    return render(request,'request_list/request_list.html',context)

