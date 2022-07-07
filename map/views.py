from multiprocessing import context
from django.shortcuts import render
from requests import request
import folium

# Create your views here.

def show_map(request):
    # create map object
    m = folium.Map(location=[19,-12], zoom_start=2)
    folium.Marker([5.594, -0.219], tooltip='Click for more',
                    popup='Ghana').add_to(m)
    # Get HTML represent
    m = m._repr_html_()
    context = {
        'm':m,
    }
    return render(request, 'map/map.html',context)