```python
from django.test import TestCase
from .models import Payment

class PaymentTestCase(TestCase):
    def setUp(self):
        Payment.objects.create(payment_method="Paypal", amount=100.00, transaction_id="1234567890")
        Payment.objects.create(payment_method="Stripe", amount=200.00, transaction_id="0987654321")

    def test_payment_methods(self):
        paypal = Payment.objects.get(payment_method="Paypal")
        stripe = Payment.objects.get(payment_method="Stripe")
        self.assertEqual(paypal.get_payment_method(), "The payment method is Paypal.")
        self.assertEqual(stripe.get_payment_method(), "The payment method is Stripe.")

    def test_payment_amount(self):
        paypal = Payment.objects.get(payment_method="Paypal")
        stripe = Payment.objects.get(payment_method="Stripe")
        self.assertEqual(paypal.get_payment_amount(), "The payment amount is 100.00.")
        self.assertEqual(stripe.get_payment_amount(), "The payment amount is 200.00.")

    def test_transaction_id(self):
        paypal = Payment.objects.get(payment_method="Paypal")
        stripe = Payment.objects.get(payment_method="Stripe")
        self.assertEqual(paypal.get_transaction_id(), "The transaction id is 1234567890.")
        self.assertEqual(stripe.get_transaction_id(), "The transaction id is 0987654321.")
```