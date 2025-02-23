from decimal import Decimal

from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response

from .constanst import TradeTypeConst
from .models import Transaction


class CalculateStockStatusService:

    def execute(self, request):
        """Calculate FIFO based balance quantity and average buy price"""
        trade_date = request.query_params.get('trade_date', None)
        company = request.query_params.get('company', None)
        if not trade_date or not company:
            return Response({"error": "trade_date and company are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            trade_date = timezone.datetime.strptime(trade_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        transactions = Transaction.objects.filter(company=company, trade_date__lte=trade_date).order_by('trade_date')
        inventory = []
        balance_qty = 0
        total_value = Decimal(0)

        for transaction in transactions:
            if transaction.trade_type == TradeTypeConst.BUY.value:
                inventory.append({'quantity': transaction.quantity, 'price': transaction.price})
                balance_qty += transaction.quantity
                total_value += transaction.quantity * transaction.price

            elif transaction.trade_type == TradeTypeConst.SELL.value:
                sold_qty = transaction.quantity
                while sold_qty > 0 and inventory:
                    first_batch = inventory[0]
                    if first_batch['quantity'] <= sold_qty:
                        sold_qty -= first_batch['quantity']
                        balance_qty -= first_batch['quantity']
                        total_value -= first_batch['quantity'] * first_batch['price']
                        inventory.pop(0)
                    else:
                        first_batch['quantity'] -= sold_qty
                        balance_qty -= sold_qty
                        total_value -= sold_qty * first_batch['price']
                        sold_qty = 0

            elif transaction.trade_type == TradeTypeConst.SPLIT.value:
                ratio_parts = transaction.split_ratio.split(':')
                if len(ratio_parts) != 2:
                    return Response({"error": "Invalid split ratio format. Use 'old:new'"},
                                    status=status.HTTP_400_BAD_REQUEST)

                old_ratio, new_ratio = int(ratio_parts[0]), int(ratio_parts[1])
                multiplier = new_ratio / old_ratio

                new_inventory = []
                for batch in inventory:
                    batch['quantity'] = int(batch['quantity'] * multiplier)
                    batch['price'] = batch['price'] / Decimal(multiplier)
                    new_inventory.append(batch)

                inventory = new_inventory
                balance_qty = int(balance_qty * multiplier)

        avg_buy_price = total_value / balance_qty if balance_qty > 0 else Decimal(0)
        return Response({"balance_qty": balance_qty, "avg_buy_price": avg_buy_price})
