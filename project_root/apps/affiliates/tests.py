```python
from django.test import TestCase
from .models import AffiliateAccount

class AffiliateAccountModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        AffiliateAccount.objects.create(name='Test Affiliate', affiliate_id='123456')

    def test_name_label(self):
        affiliate = AffiliateAccount.objects.get(id=1)
        field_label = affiliate._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_affiliate_id_label(self):
        affiliate = AffiliateAccount.objects.get(id=1)
        field_label = affiliate._meta.get_field('affiliate_id').verbose_name
        self.assertEquals(field_label, 'affiliate_id')

    def test_name_max_length(self):
        affiliate = AffiliateAccount.objects.get(id=1)
        max_length = affiliate._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_object_name_is_name(self):
        affiliate = AffiliateAccount.objects.get(id=1)
        expected_object_name = f'{affiliate.name}'
        self.assertEquals(expected_object_name, str(affiliate))
```