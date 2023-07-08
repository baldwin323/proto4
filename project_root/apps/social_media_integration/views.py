```python
from django.shortcuts import render
from .models import SocialMediaAccount
from django.http import JsonResponse
from django.views import View
from .services import SocialMediaService

class SocialMediaView(View):
    def get(self, request, *args, **kwargs):
        social_media_accounts = SocialMediaAccount.objects.all()
        return JsonResponse({'social_media_accounts': list(social_media_accounts.values())})

    def post(self, request, *args, **kwargs):
        service = SocialMediaService()
        response = service.connect_to_social_media(request.data)
        return JsonResponse(response)

    def put(self, request, *args, **kwargs):
        service = SocialMediaService()
        response = service.update_social_media_account(request.data)
        return JsonResponse(response)

    def delete(self, request, *args, **kwargs):
        service = SocialMediaService()
        response = service.delete_social_media_account(request.data)
        return JsonResponse(response)
```