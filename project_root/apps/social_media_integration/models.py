```python
from django.db import models
from django.contrib.auth.models import User

class SocialMediaAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    api_key = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.platform

class Post(models.Model):
    account = models.ForeignKey(SocialMediaAccount, on_delete=models.CASCADE)
    content = models.TextField()
    post_type = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

class Message(models.Model):
    account = models.ForeignKey(SocialMediaAccount, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=50)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]
```