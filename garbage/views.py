from django.shortcuts import render
from rest_framework.views import APIView
from random import randrange
from rest_framework.response import Response
# Create your views here.

class GarbageList(APIView):
    def post(self, request):
        label_no = randrange(6)
        return Response(label_no)
