from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Transaction

class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for the Register User model."""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        """Create a new user with encrypted password"""
        user = User.objects.create_user(**validated_data)
        return user


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for the Transaction model."""
    class Meta:
        model = Transaction
        fields = '__all__'
