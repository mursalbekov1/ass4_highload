from django.test import TestCase
from .models import SecureData

class SecureDataTest(TestCase):
    def test_valid_data(self):
        data = SecureData.objects.create(name="Test User", age=25, website="https://example.com")
        self.assertEqual(data.name, "Test User")
