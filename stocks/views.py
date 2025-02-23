from rest_framework import generics

from .models import Transaction
from .serializer import TransactionSerializer
from .calculate_stock_status_service import CalculateStockStatusService


class TransactionView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CalculatePortfolioView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        """Get balance quantity and average buy price for a company"""
        response = CalculateStockStatusService().execute(request)
        return response
