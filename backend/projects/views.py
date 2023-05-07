from django.shortcuts import render
from .models import ProjectDetails
from .serializers import ProjectDetailsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class ProjectDetailView(APIView):
    def post(self, requrest):
        context = {
            'val2': 2
        }

        return Response(context)

    def get(self, request):

        return Response
