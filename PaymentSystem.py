from enum import Enum
from PaymentHandlers import ProcessPayPal
from PaymentHandlers import ProcessGooglePay
from PaymentHandlers import ProcessCreditCard
class PaymentMode(Enum):
  PayPal="PAYPAL"
  GooglePay="GOOGLEPAY"
  CreditCard="CREDITCARD"

def checkout(mode,amount):
  if mode.upper()==PaymentMode.PayPal.value:
    return ProcessPayPal(amount)
  elif mode.upper()==PaymentMode.GooglePay.value:
    return ProcessGooglePay(amount)
  elif mode.upper()==PaymentMode.CreditCard.value:
    return ProcessCreditCard(amount)
