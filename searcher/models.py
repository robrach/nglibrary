from django.db import models


class Author(models.Model):
    author_key = models.CharField(max_length=50)
    personal_name = models.CharField(max_length=100)
    alternate_names = models.TextField(default='')
    view_count = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.personal_name}, {self.view_count}'
