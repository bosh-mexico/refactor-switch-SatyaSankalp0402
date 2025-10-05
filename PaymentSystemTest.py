import unittest
from PaymentSystem import PaymentMode, checkout
class TestCheckout(unittest.TestCase):
  def test_checkout_paypal(self):
    result=checkout(PaymentMode.PAYPAL,100)
    self.assertEqual(result,"Processed PayPal payment amount of $100")
  def test_checkout_googlepay(self):
    result=checkout(PaymentMode.GOOGLEPAY,200)
    self.assertEqual(result,"Processed GooglePay payment amount of $200")
  def test_checkout_creditcard(self):
    result=checkout(PaymentMode.CREDITCARD,10000)
    self.assertEqual(result,"Processed CreditCard payment amount of $10000")
  def test_checkout_invalid(self):
    result=checkout(PaymentMode.UNKNOWN,4000)
    self.assertEqual(result,"Invalid Payment Mode Selected")
