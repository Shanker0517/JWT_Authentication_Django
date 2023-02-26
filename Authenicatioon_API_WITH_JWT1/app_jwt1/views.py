from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializer import *
from django.contrib.auth import authenticate
from .renders import UserRenderers
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
class UserRegistionView(APIView):
    renderer_classes=[UserRenderers]
    def post(self,request,format=None):
        serializer=UserRegistionViewSerialzer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registrationn Successful'},status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UserLoginView(APIView):
    renderer_classes=[UserRenderers]
    def post(self,request,format=None):
        serializer=UserLoginViewSerialzer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,'msg':'login Success'},status=status.HTTP_200_OK,)
            else:
                return Response({'errors':{'non_fields':['Email or Password is not valid']}},status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


