from enum import Enum
from PaymentHandlers import ProcessPayPal
class PaymentMode(Enum):
  PayPal="PAYPAL"

def checkout(mode,amount):
  if mode.upper()==PaymentMode.PayPal.value:
    return ProcessPayPal(amount)
