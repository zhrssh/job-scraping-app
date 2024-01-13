from django.http import HttpResponse


def index(request):
    # Renders the html template that allows users
    # to access the webscraper
    return HttpResponse("OK")
