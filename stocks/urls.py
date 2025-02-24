from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView, TransactionView, CalculatePortfolioView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('transactions/', TransactionView.as_view(), name='transactions'),
    path('portfolio/', CalculatePortfolioView.as_view(), name='portfolio'),
]