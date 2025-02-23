from enum import Enum

class TradeTypeConst(Enum):
    """ Trade type constant enumeration """
    BUY = "BUY"
    SELL = "SELL"
    SPLIT = "SPLIT"

    @classmethod
    def choices(cls):
        """ Returns choices for Django model field """
        return [(tag.value, tag.name.capitalize()) for tag in cls]
