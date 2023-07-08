```python
from django.test import TestCase
from .models import Target

class TargetModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Target.objects.create(name='Test Target', description='This is a test target')

    def test_name_content(self):
        target = Target.objects.get(id=1)
        expected_object_name = f'{target.name}'
        self.assertEquals(expected_object_name, 'Test Target')

    def test_description_content(self):
        target = Target.objects.get(id=1)
        expected_object_description = f'{target.description}'
        self.assertEquals(expected_object_description, 'This is a test target')

class TargetViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Target.objects.create(name='Test Target', description='This is a test target')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/targeting/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('targeting'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('targeting'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'targeting/target.html')
```