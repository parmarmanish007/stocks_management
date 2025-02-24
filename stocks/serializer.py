from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    """Serializer for the Transaction model."""
    class Meta:
        model = Transaction
        fields = '__all__'
