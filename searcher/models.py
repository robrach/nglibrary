from django.db import models


class Author(models.Model):
    key = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    view_count = models.IntegerField(default=1)
