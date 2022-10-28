from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Page(models.Model):
    page_last_update = models.DateField(name='last_updated', auto_now=True)
    page_title = models.CharField(max_length=50)
    page_name = models.CharField(max_length=30)
    page_overview = models.TextField(max_length=350)
    page_body_text = models.TextField(max_length=5000)
    published = models.BooleanField(default=False)

    class PageTypes(models.TextChoices):
        main = 'main', _('Main')
        challenge = 'challenge', _('Challenge')

    page_type = models.CharField(
        max_length=10,
        choices=PageTypes.choices,
        default=PageTypes.main
    )

    def __str__(self):
        return f'{self.page_name}_Page'


class Challenges(Page):
    github_repo = models.CharField(max_length=100)
    live_link = models.CharField(max_length=150)

