import os
# This needs to be done to get PyCharm to recognize the Django environment and run Django tests properly.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NOABackend1.settings')
os.environ.setdefault('ENVIRONMENT', 'test')  # Set the environment to 'test' for testing purposes
import django
django.setup()

from django.test import TestCase

# Get the EXTERNAL_API_URL from the settings
from django.conf import settings

# Create your tests here.

class DadJokesFromAPI(TestCase):
    """
    Test case for the Dad Jokes API.
    """

    def setUp(self):
        self.api_url = settings.EXTERNAL_API_URL

    def test_get_joke(self):
        """
        Test that we can retrieve a joke from the API.
        """
        # Here you would typically make a request to the API and check the response
        # For example:
        # response = self.client.get('/api/dad-jokes/')
        # self.assertEqual(response.status_code, 200)
        # self.assertIn('joke', response.json())
        print("This is a placeholder for the actual API test.")
        print(self.api_url)