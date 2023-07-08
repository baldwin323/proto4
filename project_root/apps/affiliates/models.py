```python
from django.db import models
from django.contrib.auth.models import User

class Affiliate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    affiliate_id = models.CharField(max_length=100, unique=True)
    earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username
```