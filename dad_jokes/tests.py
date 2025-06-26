"""Tests for the Dad Jokes API."""

# This is a hack that needs to be done to get PyCharm to recognize the Django environment and run Django tests properly.
# It also needs to be the first thing in the file, before any imports that depend on Django settings.
# -------------
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NOABackend1.settings')
os.environ.setdefault('ENVIRONMENT', 'dev')  # Set the environment to 'test' for testing purposes
import django
django.setup()
# -------------

import requests
from django.test import TestCase
from django.conf import settings  # Get the EXTERNAL_API_URL from the settings
from django.urls import reverse
from dad_jokes.utils import get_dad_joke_from_api
from unittest.mock import patch
from dad_jokes.models import DadJoke
from dad_jokes.utils import DadJoke as DadJokeObj


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

    def test_get_joke_util(self):
        """Get a joke using the utility function."""
        dad_joke = get_dad_joke_from_api()
        self.assertIsInstance(dad_joke.joke, str)
        self.assertIsInstance(dad_joke.site_id, str)
        self.assertGreater(len(dad_joke.joke), 0)

    @patch('dad_jokes.views.get_dad_joke_from_api')
    def test_store_dad_joke_through_view(self, mock_get_joke):

        # TODO: This test does not seem to run the django test database setup properly.
        # TODO: I can run the tests using the command line, but I would really like to be able to run them from PyCharm.
        dad_joke = DadJokeObj(joke="Test joke", site_id="12345")
        mock_get_joke.return_value = dad_joke

        resp = self.client.get(reverse('dad_jokes:store_dad_joke_from_api'))

        self.assertTrue(DadJoke.objects.filter(site_id='12345').exists())

