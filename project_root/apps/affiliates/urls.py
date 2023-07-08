```python
from django.urls import path
from . import views

app_name = 'affiliates'

urlpatterns = [
    path('create/', views.AffiliateCreateView.as_view(), name='affiliate_create'),
    path('update/<int:pk>/', views.AffiliateUpdateView.as_view(), name='affiliate_update'),
    path('detail/<int:pk>/', views.AffiliateDetailView.as_view(), name='affiliate_detail'),
    path('delete/<int:pk>/', views.AffiliateDeleteView.as_view(), name='affiliate_delete'),
]
```