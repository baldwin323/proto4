```python
from django.test import TestCase
from .models import DatingSiteAccount

class DatingSiteAccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        DatingSiteAccount.objects.create(username='testuser', password='testpassword123')

    def test_username_label(self):
        account = DatingSiteAccount.objects.get(id=1)
        field_label = account._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_password_label(self):
        account = DatingSiteAccount.objects.get(id=1)
        field_label = account._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')

    def test_object_name_is_username(self):
        account = DatingSiteAccount.objects.get(id=1)
        expected_object_name = f'{account.username}'
        self.assertEqual(expected_object_name, str(account))

class DatingSiteIntegrationViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        DatingSiteAccount.objects.create(username='testuser', password='testpassword123')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/dating_site_integration/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get('/dating_site_integration/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dating_site_integration/index.html')
```