from Enum import Enum
class PaymentMode(Enum):
  PayPal=1

payment_handlers={
  PaymentMode.PayPal:process_paypal

