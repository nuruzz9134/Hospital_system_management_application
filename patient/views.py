from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

from patient.serializer import ProfileSerializers

from patient.models import Customerprofile





class ProfileCreatViews(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        serializer = ProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Profile Creat Successfull"}, status=HTTP_201_CREATED)
        else:
            return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)





class ProfiletListView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                data = Customerprofile.objects.all()
                serializer = ProfileSerializers(data,many=True)
                return Response(serializer.data)

        except Exception as e:
            return Response({"msz": str(e)}, status=HTTP_400_BAD_REQUEST)





class ProfileUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    def put(self,request,pk):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                id = Customerprofile.objects.get(id=pk)
                serializer = ProfileSerializers(id,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                    return Response(repr(serializer.errors), status=HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"msz": str(e)}, status=HTTP_400_BAD_REQUEST)





class ProfileDeleteView(APIView):
    permission_classes = (IsAuthenticated,)
    def delete(self,request,pk):
        try:
            a=request.user.is_admin
            if str(a)=="True":
                id = Customerprofile.objects.get(id=pk)
                id.delete()
                return Response({'msz':'delete successful'})
        except Exception as e:
            return Response({"msz": str(e)}, status=HTTP_400_BAD_REQUEST)