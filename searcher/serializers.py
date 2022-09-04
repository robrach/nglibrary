from .models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['author_key', 'personal_name', 'alternate_names', 'view_count']
