from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    return render(request, 'home.html')


def get_interests(request):
    print(request.GET["url"])
    return JsonResponse({
        "data": [
            "Music",
            "Sports",
            "Politics",
            "Troll",
            "News",
        ]
    })


def generate_tweet(request):
    print(request.GET)
    return JsonResponse({
        "data": "This is a LLM generated tweet. Enjoy!"
    })