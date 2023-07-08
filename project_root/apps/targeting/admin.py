```python
from django.contrib import admin
from .models import Targeting

@admin.register(Targeting)
class TargetingAdmin(admin.ModelAdmin):
    list_display = ('id', 'target_area', 'target_demographic', 'target_interest')
    search_fields = ('target_area', 'target_demographic', 'target_interest')
    list_filter = ('target_area', 'target_demographic', 'target_interest')
```