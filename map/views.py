from cgitb import html
from multiprocessing import context
from django.shortcuts import render
from requests import request
import folium
import geocoder
from request.models import Request

# Create your views here.

def show_map(request):
    address = Request.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    # create map object
    m = folium.Map(location=[19,-12], zoom_start=2)

    folium.Marker([lat, lng], tooltip='Click for more',
                    popup=address).add_to(m)
    # Get HTML represent
    m = m._repr_html_()
    context = {
        'm':m,
    }
    return render(request, 'map/map.html',context)