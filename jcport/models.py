import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Page(models.Model):
    page_last_update = models.DateField(name='last_updated')
    page_title = models.CharField(max_length=50)
    page_name = models.CharField(max_length=30)
    page_overview = models.TextField(max_length=350)
    page_body_text = models.TextField(max_length=5000)
    page_type = models.TextChoices('main', 'project')
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.page_name}_Page'

    def was_recently_updated(self):
        return self.page_last_update >= timezone.now - datetime.delta(days=7)


