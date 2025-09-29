import unittest
from PaymentSystem import checkout
class TestCheckout(unittest.TestCase):
  def test_checkout_paypal(self):
    result=checkout("PayPal",100)
    self.assertEqual(result,"Processed PayPal payment amount of $100")
  
