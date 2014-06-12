__author__ = 'koke07'
# -*- coding : utf-8 -*-
from rest_framework.views import APIView
from django.contrib.auth.models import User
from serializers import UserSerializer, PhotoSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404
from rest_framework import status
from models import Photo

class UserListApi(APIView):

    def get(self,request):

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    def post(self,request):

        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserDetailApi(APIView):

     def get(self,request,pk):

        user = get_object_or_404(User,pk=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)

     def put(self,request,pk):

         user = get_object_or_404(User,pk=pk)
         serializer = UserSerializer(user,data=request.DATA)

         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_200_OK)
         else:
             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

     def delete(self, request,pk):
         user = get_object_or_404(User,pk=pk)
         user.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)



class PhotoListApi(ListCreateAPIView):

   queryset = Photo.objects.all()
   serializer_class = PhotoSerializer