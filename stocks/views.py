from rest_framework import generics

from .models import Transaction
from .serializer import TransactionSerializer
from .calculate_stock_status_service import CalculateStockStatusService


class TransactionView(generics.CreateAPIView):
    """API view to create a new transaction."""
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class CalculatePortfolioView(generics.RetrieveAPIView):
    """API view to calculate portfolio status (balance quantity and average buy price)."""

    def get(self, request, *args, **kwargs):
        """Get balance quantity and average buy price for a company."""
        response = CalculateStockStatusService().execute(request)
        return response
