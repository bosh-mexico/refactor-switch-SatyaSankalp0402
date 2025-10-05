class PayPalPayment:
  def ProcessPayment(self,amount):
    return f"Processed PayPal payment amount of ${amount}"
    #Add PayPal Specific Logic Here
class GooglePayPayment:
  def ProcessPayment(self,amount):
    return f"Processed GooglePay payment amount of ${amount}"
    #Add GooglePay Specific Logic Here
class CreditCardPayment:
  def ProcessPayment(self,amount):
    return f"Processed CreditCard payment amount of ${amount}"
    #Add CreditCard Specific Logic Here
class UnknownPayment:
  def ProcessPayment(self,amount):
    return "Invalid Payment Mode Selected!"
