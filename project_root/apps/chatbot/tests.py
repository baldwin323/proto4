```python
from django.test import TestCase
from .models import ChatBot

class ChatBotModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ChatBot.objects.create(name='Test Bot', description='This is a test bot')

    def test_name_content(self):
        bot = ChatBot.objects.get(id=1)
        expected_object_name = f'{bot.name}'
        self.assertEquals(expected_object_name, 'Test Bot')

    def test_description_content(self):
        bot = ChatBot.objects.get(id=1)
        expected_object_description = f'{bot.description}'
        self.assertEquals(expected_object_description, 'This is a test bot')

class ChatBotViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        ChatBot.objects.create(name='Test Bot', description='This is a test bot')

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/chatbot/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('chatbot'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('chatbot'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'chatbot/chatbot.html')
```