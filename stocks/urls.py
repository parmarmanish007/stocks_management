from django.urls import path

from .views import TransactionView, CalculatePortfolioView

urlpatterns = [
    path('transactions/', TransactionView.as_view(), name='transactions'),
    path('portfolio/', CalculatePortfolioView.as_view(), name='portfolio'),
]