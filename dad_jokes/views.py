import json
from django.shortcuts import render
from django.http import HttpResponse

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
        resp = HttpResponse(f"Stored new dad joke: {new_dad_joke.joke}")
    else:
        # TODO: Log if the joke already exists
        resp = HttpResponse(f"Joke with ID {dad_joke.site_id} already exists. Not storing again.")

    return resp

def locally_stored_dad_joke(request, joke_id):
    """
    Handle GET, PUT, DELETE requests for a dad joke with the given ID.
    """
    if request.method == 'GET':
        try:
            dad_joke = DadJoke.objects.get(id=joke_id)
            return HttpResponse(f"Retrieved dad joke: {dad_joke.joke}")
        except DadJoke.DoesNotExist:
            return HttpResponse("Dad joke not found.", status=404)

    elif request.method == 'PUT':
        # Update the joke text
        joke_text = json.loads(request.body).get('joke')
        if joke_text:
            try:
                dad_joke = DadJoke.objects.get(id=joke_id)
                dad_joke.joke = joke_text
                dad_joke.save()
                return HttpResponse(f"Updated dad joke: {dad_joke.joke}")
            except DadJoke.DoesNotExist:
                return HttpResponse("Dad joke not found.", status=404)
        else:
            return HttpResponse("No joke text provided.", status=400)

    elif request.method == 'DELETE':
        # Delete the joke
        try:
            dad_joke = DadJoke.objects.get(id=joke_id)
            dad_joke.delete()
            return HttpResponse("Dad joke deleted successfully.")
        except DadJoke.DoesNotExist:
            return HttpResponse("Dad joke not found.", status=404)

    else:
        return HttpResponse("Method not allowed.", status=405)

def store_new_dad_joke(request):
    """
    Stores a dad joke that is not from the external API.
    Since the joke is not from the API, it will be stored with a local site_id.
    """
    if request.method == 'POST':
        joke_text = json.loads(request.body).get('joke')
        if joke_text:
            new_dad_joke = DadJoke(joke=joke_text, site_id="local_" + str(DadJoke.objects.count() + 1))
            new_dad_joke.save()
            return HttpResponse(f"Stored new dad joke: {new_dad_joke.joke}")
        else:
            return HttpResponse("No joke text provided.", status=400)
    else:
        return HttpResponse("Method not allowed.", status=405)