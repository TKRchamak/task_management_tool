from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        ]

    def validate(self, data):
        print("data on serializer: ", data)
        return data

    def create(self, data):
        user_data = User.objects.create(
            username=data['username'],
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
        )

        user_data.set_password(data['password'])
        user_data.save()

        return user_data
