from django.test import TestCase
from django.utils.timezone import now
from datetime import timedelta

from jcport import models


# Create your tests here.
class PageModelTest(TestCase):
    new_page_data = {
        'page_title': 'Test Page',
        'page_name': 'test_page',
        'page_overview': 'Testing page creation.',
        'page_body_text': 'Testing some page creation body.',
        'published': False,
    }
    test_page = models.Page(**new_page_data)

    def test_page_created(self):
        assert(isinstance(self.test_page, models.Page))

    def test_page_title(self):
        page_title = self.test_page.page_title

        assert(isinstance(page_title, str))
        assert(len(page_title) <= 50)

    def test_page_name(self):
        page_name = self.test_page.page_name

        assert(' ' not in str(page_name))
        assert(isinstance(page_name, str))
        assert(len(page_name) <= 30)

    def test_page_overview(self):
        page_overview = self.test_page.page_overview

        assert(isinstance(page_overview, str))
        assert(len(page_overview) <= 350)

    def test_page_body_text(self):
        page_body_text = self.test_page.page_body_text

        assert(isinstance(page_body_text, str))
        assert(len(page_body_text) <= 350)

    def test_published(self):
        published = self.test_page.published

        assert(isinstance(published, bool))

    def test_str_func(self):
        page_str = self.test_page.__str__()

        assert(isinstance(page_str, str))
        assert(page_str == self.test_page.__str__())
