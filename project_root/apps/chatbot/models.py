```python
from django.db import models
from django.contrib.auth.models import User

class ChatBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)
    api_secret = models.CharField(max_length=200)
    access_token = models.CharField(max_length=200)
    access_token_secret = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Content(models.Model):
    bot = models.ForeignKey(ChatBot, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)  # art, pics, vids, subscriptions
    content_file = models.FileField(upload_to='content_files/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.type

class SocialMediaAccount(models.Model):
    bot = models.ForeignKey(ChatBot, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)  # social media platform name
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.platform

class DatingSiteAccount(models.Model):
    bot = models.ForeignKey(ChatBot, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.site_name
```