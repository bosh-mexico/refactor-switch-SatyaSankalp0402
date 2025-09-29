from enum import Enum
from PaymentHandlers import ProcessPayPal
class PaymentMode(Enum):
  PayPal="PayPal"

def checkout(mode,amount):
  if mode==PaymentMode.PayPal:
    ProcessPayPal(amount)
