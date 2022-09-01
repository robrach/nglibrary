from django.db import models


class Author(models.Model):
    author_key = models.CharField(max_length=50)
    personal_name = models.CharField(max_length=100)
    view_count = models.IntegerField(default=1)
