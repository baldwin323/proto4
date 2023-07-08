```python
from django.contrib import admin
from .models import ChatBot

class ChatBotAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'created_at', 'updated_at']
    list_filter = ['status']
    search_fields = ['name']

admin.site.register(ChatBot, ChatBotAdmin)
```