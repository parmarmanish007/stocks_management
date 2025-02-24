from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Transaction
from .serializer import TransactionSerializer, RegisterUserSerializer
from .calculate_stock_status_service import CalculateStockStatusService


class RegisterView(generics.CreateAPIView):
    """API view to create a new user."""
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]


class TransactionView(generics.CreateAPIView):
    """API view to create a new transaction."""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]


class CalculatePortfolioView(generics.RetrieveAPIView):
    """API view to calculate portfolio status (balance quantity and average buy price)."""
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """Get balance quantity and average buy price for a company."""
        response = CalculateStockStatusService().execute(request)
        return response
