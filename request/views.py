from .models import Request
# from msilib.schema import Class
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Request
from .serializers import LocationSerializer, RequestSerializer,ComplainSerializer
from request import serializers
from rest_framework import status
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
import requests
from complain.models import Complain
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse
import subprocess
import os

class Request(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView, mixins.RetrieveModelMixin):

    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def get(self, request, pk=None):
        if (pk) :
            print( "sdasadsa", pk);
            return self.retrieve(request)
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        req =self.update(request, *args, **kwargs)
        print(request.data["mobile_no"])
        r = requests.get("https://app.notify.lk/api/v1/send?user_id=23370&api_key=VcYYcYck6rUJbMx6WiRJ&sender_id=NotifyDEMO&to=94"+str(request.data["mobile_no"])+"&message=Your  garbage collected")

        print(r.json())
        return req

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class Complain(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView, mixins.RetrieveModelMixin):

    serializer_class = ComplainSerializer
    queryset = Complain.objects.all()

    def get(self, request, pk=None):
        if (pk) :

            return self.retrieve(request)
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        req =self.update(request, *args, **kwargs)
        return req

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class ImageClasifier(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView, mixins.RetrieveModelMixin):



    def post(self, request, *args, **kwargs):

        file_obj = request.FILES['image']
        file = file_obj.read()
        default_storage.save('temp/temp.jpg', ContentFile(file))

        a=subprocess.call("python3 validateImg.py", shell=True)


        print (a)



        try:
            f = open("temp/res.txt", "r")
            result = f.read()
            print(result)
            f.close()
            if result == "Garbage":

                a = subprocess.call("python3 main.py", shell=True)

                print(a)
                if os.path.exists("temp/temp.jpg"):
                    os.remove("temp/temp.jpg")

                f = open("temp/res.txt", "r")
                result = f.read()
                print(result)
                f.close()
        except Exception as e:
            print (e)
            result = "Not Garbage"



        if os.path.exists("temp/temp.jpg"):
            os.remove("temp/temp.jpg")
        if os.path.exists("temp/res.txt"):
            os.remove("temp/res.txt")

        return JsonResponse({'status': 'SUCCESS','result': result})
#



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
        


# class RequestCount(APIView):
#     def get(self,pid):
#         count = models.Request.objects.filter(username='username', status=0).count()
#         return count