from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print("data: ", request.data.get("username"))
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user_auth = authenticate(request, username=username, password=password)

        if user_auth:
            login(request, user_auth)
            token, created = Token.objects.get_or_create(user=user_auth)
        context = {
            "token":token.key
        }
        return Response(context)