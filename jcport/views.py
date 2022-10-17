from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from . models import Page


# Create your views here.
def landing(request):
    pages = Page.objects.filter(published=True)
    context = {}

    for page in pages:
        context[page.page_name] = page



    template = loader.get_template('jcport/index.html')

    return HttpResponse(template.render(context, request))


def contact(request):
    pass