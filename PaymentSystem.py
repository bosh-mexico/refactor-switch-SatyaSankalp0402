from enum import Enum
from PaymentHandlers import PayPalPayment, GooglePayPayment, CreditCardPayment, UnknownPayment

class PaymentMode(Enum):
  PayPal=1
  GooglePay=2
  CreditCard=3
  UNKOWN=99

payment_methods = {  
    PaymentMode.PAYPAL: PayPalPayment(),
    PaymentMode.GOOGLEPAY: GooglePayPayment(),
    PaymentMode.CREDITCARD: CreditCardPayment(),
    PaymentMode.UNKNOWN: UnknownPayment()
  }
def checkout(mode,amount):
  payment_handler=payment_methods.get(mode)
  payment_handler.process(amount)
