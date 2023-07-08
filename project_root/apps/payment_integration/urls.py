```python
from django.urls import path
from . import views

urlpatterns = [
    path('process_payment/', views.process_payment, name='process_payment'),
    path('payment_done/', views.payment_done, name='payment_done'),
    path('payment_canceled/', views.payment_canceled, name='payment_canceled'),
]
```