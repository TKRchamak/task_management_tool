from django.shortcuts import render
from .models import ProjectDetails
from .serializers import ProjectDetailsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

# Create your views here.


class ProjectDetailListCreate(generics.ListCreateAPIView):
    ''' create single detail and get list of details'''
    serializer_class = ProjectDetailsSerializer
    queryset = ProjectDetails.objects.all()

class ProjectDetailOperation(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectDetailsSerializer
    queryset = ProjectDetails.objects.all()
