from django.http import HttpResponse
from django.template import loader
from . models import Page


# Create your views here.
def landing(request):
    pages = Page.objects.filter(published=True)
    context = {}

    for page in pages:
        context[page.page_name] = page # pragma: no cover

    template = loader.get_template('jcport/index.html')

    return HttpResponse(template.render(context, request))


def challenge(request):
    pass


def contact(request):
    pass # pragma: no cover