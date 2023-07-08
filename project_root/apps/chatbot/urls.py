```python
from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('connect/', views.connect, name='connect'),
    path('train/', views.train, name='train'),
    path('sell/', views.sell, name='sell'),
    path('flirt/', views.flirt, name='flirt'),
    path('map/', views.map, name='map'),
    path('target/', views.target, name='target'),
    path('login/', views.login, name='login'),
]
```