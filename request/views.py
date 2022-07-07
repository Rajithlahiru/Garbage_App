import imp
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Request
from .serializers import RequestSerializer

# Create your views here.
class RequestList(APIView):

    def get(self,request):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests,many=True)
        return Response(serializer.data)

    def post(self):
        pass