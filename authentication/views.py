from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,RegisterSerializer,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from user_register.models  import User
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from django.http import HttpResponse
import json
from django.http import JsonResponse
# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Register(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView, mixins.RetrieveModelMixin):

    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    def get(self, request, pk=None):
        if (pk) :
            print( "sdasadsa", pk);
            return self.retrieve(request)
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




class Login(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView, mixins.RetrieveModelMixin):

    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def get(self, request, pk=None):
        queryset = User.objects.all()
        if (pk) :
            print( "sdasadsa", pk);
            return queryset.filter(id=1)
            return self.retrieve(request)
        return self.list(request)

    def post(self, request, *args, **kwargs):
        queryset = User.objects.all()
        print(queryset.filter(email=request.data['email'],password=request.data['password']))
        try:
            return JsonResponse({'status': 'SUCCESS','id':queryset.filter(email=request.data['email'],password=request.data['password'])[0].id})
        except:
            return JsonResponse({'status': 'Someting Went Wrang'})





        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


