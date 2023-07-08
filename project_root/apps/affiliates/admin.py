```python
from django.contrib import admin
from .models import AffiliateAccount

@admin.register(AffiliateAccount)
class AffiliateAccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'affiliate_id', 'affiliate_link')
    search_fields = ('user__username', 'affiliate_id')
    list_filter = ('user',)
```