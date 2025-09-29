import unittest
from PaymentSystem import checkout
class TestCheckout(unittest.TestCase):
  def test_checkout_paypal(self):
    result=checkout("PayPal",100)
    self.assertEqual(result,"Processed PayPal payment amount of $100")
    result=checkout("Paypal",150)
    self.assertEqual(result,"Processed PayPal payment amount of $150")
  def test_checkout_googlepay(self):
    result=checkout("GooglePay",200)
    self.assertEqual(result,"Processed GooglePay payment amount of $200")
