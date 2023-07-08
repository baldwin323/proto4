```python
from django.db import models
from django.contrib.auth.models import User

class DatingSite(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)
    api_secret = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DatingSiteAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dating_site = models.ForeignKey(DatingSite, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} - {self.dating_site.name}'

class Content(models.Model):
    account = models.ForeignKey(DatingSiteAccount, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.account.user.username} - {self.type}'
```