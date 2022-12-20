from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from registration.serializations import (superuserSerializer,
                                        UserRegistrationSerializer,
                                        UserLoginSerializer,
                                        )
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



# Create your views here.



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }




class Creatsuperuserview(APIView):
    def post (self,request,format=None):
        serializer = superuserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            superuser = serializer.save()
            token = get_tokens_for_user(superuser)
            return Response(
                {'token':token, 'msg': 'super user creat Successfull'},
                status = status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserRegistrationView(APIView):
    def post (self,request,format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {'token':token, 'msg': 'Registration Successfull'},
                status = status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            phone = serializer.data.get('phone')
            password = serializer.data.get('password')
            user = authenticate(phone=phone, password=password)
            token = get_tokens_for_user(user)
            if user is not None:
                return Response(
                    {'token':token,'msg': 'Login Successfull'},
                    status = status.HTTP_200_OK
                )

            else:
                return Response(
                    {'errors': {'non_field_error': ['phone or Password is not valid']}},
                    status = status.HTTP_400_BAD_REQUEST)
