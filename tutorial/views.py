from django.shortcuts import render
from .models import Book
from .serializers import Bookserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view (['GET','POST'])
def Book_list(request): 
    if request.method == 'GET':
       tutorial = Book.objects.all()
       serializer = Bookserializer(tutorial,many=True)
       return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = Bookserializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_201_CREATED)



@api_view (['PUT','DELETE'])
def Book_detail(request,pk):

   try:
       tutorial = Book.objects.get(id=pk)
   except Book.DoesNotExist:
       return Response(status=status.HTTP_404_NOT_FOUND)
   

   if request.method == 'PUT':
       serializer = Bookserializer(tutorial,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
       return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   

   elif request.method == 'DELETE':
       tutorial.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
      
      

