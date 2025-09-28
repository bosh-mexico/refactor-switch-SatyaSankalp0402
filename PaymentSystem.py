from Enum import Enum
from PaymentHandlers import ProcessPayPal
class PaymentMode(Enum):
  PayPal=1

payment_handlers={
  PaymentMode.PayPal:ProcessPayPal

