from enum import Enum
from PaymentHandlers import ProcessPayPal
from PaymentHandlers import ProcessGooglePay
from PaymentHandlers import ProcessCreditCard
class PaymentMode(Enum):
  PayPal="PAYPAL"
  GooglePay="GOOGLEPAY"
  CreditCard="CREDITCARD"

def checkout(mode,amount):
  payment_methods = {  
    PaymentMode.PayPal.value: ProcessPayPal,
    PaymentMode.GooglePay.value: ProcessGooglePay,
    PaymentMode.CreditCard.value: ProcessCreditCard
  }
  method=payment_methods.get(mode.upper())
  if method !=None:
    return method(value)
