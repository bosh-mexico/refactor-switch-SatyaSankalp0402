from enum import Enum
import PaymentHandlers 
class PaymentMode(Enum):
  PayPal="PAYPAL"
  GooglePay="GOOGLEPAY"

def checkout(mode,amount):
  if mode.upper()==PaymentMode.PayPal.value:
    return ProcessPayPal(amount)
  elif mode.upper()==PaymentMode.GooglePay.value:
    return ProcessGooglePay(amount)
