```python
from django.urls import path
from . import views

urlpatterns = [
    path('connect/', views.connect_social_media, name='connect_social_media'),
    path('disconnect/', views.disconnect_social_media, name='disconnect_social_media'),
    path('post/', views.post_content, name='post_content'),
    path('map/', views.map_social_media, name='map_social_media'),
    path('target/', views.target_customers, name='target_customers'),
]
```