from django.shortcuts import render

from dad_jokes.utils import get_dad_joke_from_api, DadJoke as DadJokeObj
from dad_jokes.models import DadJoke

def index(request):
    """
    Render the index page for the dad jokes app.
    """
    #TODO: Currently there is no index and possibly there should not be one.
    return render(request, 'dad_jokes/index.html')

def store_dad_joke_from_api(request):
    """
    Store a dad joke from an external API.
    If the joke already exists in the database, it will not be stored again.
    """
    dad_joke: DadJokeObj = get_dad_joke_from_api()
    # If a joke with the same ID from the API already exists we ignore it.
    if not DadJoke.objects.filter(site_id=dad_joke.site_id).exists():
        new_dad_joke = DadJoke(joke=dad_joke.joke, site_id=dad_joke.site_id)
        new_dad_joke.save()
    else:
        # TODO: Log if the joke already exists
        pass