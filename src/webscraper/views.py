from django.http import HttpResponse
from django.template import loader


def index(request):
    """Renders the html template that allows users
    to access the webscraper"""
    template = loader.get_template("index.html")

    return HttpResponse(template.render(request=request))
