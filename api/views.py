from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.response import Response
from .models import *

def home(request):
    return HttpResponse("This is homepage")

class ProjectViewSet (viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Recipes.objects.all()
    serializer_class = ProjectSerializer

    def list(self, request):
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        print("List of items:", serializer.data)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Created item:", serializer.data)
            return Response(serializer.data)
        else:
            print("Errors while creating item:", serializer.errors)
            return Response(serializer.errors, status=400)
        
    def retrieve(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project)
        print("Retrieved item:", serializer.data) 
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        project = self.queryset.get(pk=pk)
        serializer = self.serializer_class(project,data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Updated item:", serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
