```python
from django.urls import path
from . import views

app_name = 'dating_site_integration'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('push_content/', views.push_content, name='push_content'),
    path('manage_accounts/', views.manage_accounts, name='manage_accounts'),
]
```