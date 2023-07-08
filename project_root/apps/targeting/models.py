```python
from django.db import models
from django.contrib.auth.models import User

class Target(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_media_site = models.CharField(max_length=255)
    demographic = models.CharField(max_length=255)
    area_of_interest = models.CharField(max_length=255)
    deployment_mission = models.TextField()

    def __str__(self):
        return self.social_media_site

class Demographic(models.Model):
    target = models.ForeignKey(Target, related_name='demographics', on_delete=models.CASCADE)
    demographic_group = models.CharField(max_length=255)

    def __str__(self):
        return self.demographic_group

class AreaOfInterest(models.Model):
    target = models.ForeignKey(Target, related_name='areas_of_interest', on_delete=models.CASCADE)
    area = models.CharField(max_length=255)

    def __str__(self):
        return self.area
```