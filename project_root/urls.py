```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('apps.chatbot.urls')),
    path('payment/', include('apps.payment_integration.urls')),
    path('social_media/', include('apps.social_media_integration.urls')),
    path('dating/', include('apps.dating_site_integration.urls')),
    path('affiliates/', include('apps.affiliates.urls')),
    path('targeting/', include('apps.targeting.urls')),
]
```