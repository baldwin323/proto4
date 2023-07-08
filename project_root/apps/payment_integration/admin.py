```python
from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'amount', 'transaction_id', 'status')
    search_fields = ('user__username', 'payment_method', 'transaction_id')
    list_filter = ('status', 'payment_method')
```