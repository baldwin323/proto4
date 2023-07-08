```python
from django.urls import path
from . import views

app_name = 'targeting'

urlpatterns = [
    path('map/', views.map_social_media, name='map_social_media'),
    path('deploy/', views.deploy_target, name='deploy_target'),
    path('demographics/', views.manage_demographics, name='manage_demographics'),
]
```