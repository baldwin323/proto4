```python
from django.contrib import admin
from .models import DatingSiteAccount

@admin.register(DatingSiteAccount)
class DatingSiteAccountAdmin(admin.ModelAdmin):
    list_display = ('username', 'site_name', 'last_login')
    search_fields = ('username', 'site_name')
    list_filter = ('site_name',)
```