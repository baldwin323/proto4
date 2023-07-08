```python
from django.shortcuts import render
from .models import Payment
from django.http import JsonResponse
import stripe

stripe.api_key = "your_stripe_api_key"

def create_payment(request):
    if request.method == 'POST':
        payment = Payment()
        payment.user = request.user
        payment.amount = request.POST.get('amount')
        payment.save()

        return JsonResponse({'message': 'Payment created successfully.'}, status=200)

def charge(request, payment_id):
    if request.method == 'POST':
        payment = Payment.objects.get(id=payment_id)
        stripe.Charge.create(
            amount=payment.amount,
            currency='usd',
            description='Payment for content',
            source=request.POST['stripeToken']
        )

        payment.is_paid = True
        payment.save()

        return JsonResponse({'message': 'Payment processed successfully.'}, status=200)
```