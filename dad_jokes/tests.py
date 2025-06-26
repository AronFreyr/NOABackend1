"""Tests for the Dad Jokes API."""

# This is a hack that needs to be done to get PyCharm to recognize the Django environment and run Django tests properly.
# It also needs to be the first thing in the file, before any imports that depend on Django settings.
# -------------
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NOABackend1.settings')
os.environ.setdefault('ENVIRONMENT', 'test')  # Set the environment to 'test' for testing purposes
import django
django.setup()
# -------------

import requests
from django.test import TestCase
from django.conf import settings  # Get the EXTERNAL_API_URL from the settings


class DadJokesFromAPI(TestCase):
    """
    Test case for the Dad Jokes API.
    """

    def setUp(self):
        self.api_url: str = settings.EXTERNAL_API_URL

    def test_get_joke_from_api(self):
        """
        Test that we can retrieve a joke from the API.
        """
        headers = {'Accept': 'application/json'}
        resp = requests.get(self.api_url, headers=headers, timeout=1)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertIn('joke', data)
        self.assertIn('id', data)
