from enum import Enum
from PaymentHandlers import PayPalPayment, GooglePayPayment, CreditCardPayment, UnknownPayment

class PaymentMode(Enum):
  PAYPAL=1
  GOOGLEPAY=2
  CREDITCARD=3
  UNKNOWN=99

payment_methods = {  
    PaymentMode.PAYPAL: PayPalPayment(),
    PaymentMode.GOOGLEPAY: GooglePayPayment(),
    PaymentMode.CREDITCARD: CreditCardPayment(),
    PaymentMode.UNKNOWN: UnknownPayment()
  }
def checkout(mode,amount):
  payment_handler=payment_methods.get(mode)
  payment_handler.process(amount)
