import imp
from msilib.schema import Class
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Request
from .serializers import LocationSerializer, RequestSerializer
from request import serializers
from rest_framework import status

# Create your views here.

class NotFoundException(Exception):
    pass

class RequestList(APIView):

    def get(self,request):
        requests = Request.objects.all()
        serializer = RequestSerializer(requests,many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationApi(APIView):
    def get(self,request):
        locations = Request.objects.all()
        serializer = LocationSerializer(locations, many = True)
        return Response(serializer.data)
    
class RequestDetails(APIView):
    
    def get_request(self,pid):
        try:
            requests = Request.objects.get(id=pid)
            return requests
        except:
            raise NotFoundException()
            


    def get(self,request,pid):
        try:
            requests = self.get_request(pid)
            serializer = RequestSerializer(requests)
            return Response(serializer.data)

        except NotFoundException:
            return Response(status=status.HTTP_404_NOT_FOUND)

        

    def put(self,request,pid):
        try:
            requests = self.get_request(pid)
            serializer = RequestSerializer(requests, data =request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except NotFoundException:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    def delete(self, request, pid):
        try:
            requests = self.get_request(pid)
            requests.delete()
            return Response(status=status.HTTP_200_OK)

        except NotFoundException:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        
