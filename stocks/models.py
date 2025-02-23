from django.db import models
from django.utils import timezone

from .constanst import TradeTypeConst


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class Transaction(TimeStamp):
    trade_date = models.DateField(default=timezone.now)
    company = models.CharField(max_length=255)
    trade_type = models.CharField(max_length=10, choices=TradeTypeConst.choices())
    quantity = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    split_ratio = models.CharField(max_length=10, null=True, blank=True)  # e.g., "1:5"


def __str__(self):
        return f"{self.date} - {self.company} - {self.trade_type}"
