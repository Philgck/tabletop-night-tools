from django.test import TestCase
from .models import SupportMessage

class SupportMessageModelTest(TestCase):

    def setUp(self):
        SupportMessage.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            message="I need help with my account."
        )

    def test_support_message_creation(self):
        message = SupportMessage.objects.get(name="Jane Doe")
        self.assertEqual(message.email, "jane@example.com")
        self.assertEqual(message.message, "I need help with my account.")
        self.assertIsNotNone(message.created_at)

    def test_support_message_str(self):
        message = SupportMessage.objects.get(name="Jane Doe")
        self.assertEqual(str(message), "Jane Doe")