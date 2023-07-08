```python
from django.test import TestCase
from .models import SocialMediaAccount

class SocialMediaAccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SocialMediaAccount.objects.create(name='Test Account', platform='Facebook')

    def test_name_label(self):
        account = SocialMediaAccount.objects.get(id=1)
        field_label = account._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_platform_label(self):
        account = SocialMediaAccount.objects.get(id=1)
        field_label = account._meta.get_field('platform').verbose_name
        self.assertEquals(field_label, 'platform')

    def test_name_max_length(self):
        account = SocialMediaAccount.objects.get(id=1)
        max_length = account._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_name(self):
        account = SocialMediaAccount.objects.get(id=1)
        expected_object_name = f'{account.name}'
        self.assertEquals(expected_object_name, str(account))

class SocialMediaIntegrationViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SocialMediaAccount.objects.create(name='Test Account', platform='Facebook')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/social_media_integration/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/social_media_integration/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'social_media_integration/index.html')
```