from django.shortcuts import render

# Create your views here.
def show_gmap(request):
    return render(request, 'map/map.html')

