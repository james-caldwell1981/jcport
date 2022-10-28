import django.db.models
from django.test import TestCase
from django.http import HttpResponse, HttpRequest
from django.template import loader
from jcport.views import Page, landing


class LandingViewTest(TestCase):

    test_page = Page.objects.values()

    def test_query_set(self):
        assert(isinstance(self.test_page, django.db.models.QuerySet))

    def test_landing_func(self):
        request = HttpRequest
        request.method = "POST"
        request.META = {"HTTP_X_CSRFTOKEN": "abcdef1234567890abcdef1234567890"}

        try:
            test_response = landing(request)
        except ValueError as e:
            raise e('Error accessing the landing view.')
        test_resp_content = test_response.content

    def test_published_status(self):
        published_test_page = self.test_page.filter(published=True)
        unpublished_test_page = self.test_page.filter(published=False)

        pub_status = {
            'published': [],
            'unpublished': []
        }
        all_pages = published_test_page.union(unpublished_test_page)
        for status in all_pages:
            assert(isinstance(status, bool))

            if status is True:
                status['published'].append(status)
            elif status is False:
                status['unpublished'].append(status)
            else:
                raise ValueError(f'Expected \'True\' or \'False\' but received {status}')

        assert(len(pub_status['published']) == len(published_test_page))
        assert(len(pub_status['unpublished']) == len(unpublished_test_page))
