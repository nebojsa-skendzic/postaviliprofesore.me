from .models import UpdatedFiles
from rest_framework import serializers


class UpdatedFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdatedFiles
        fields = ['title', 'link', 'date', 'subjecttag', 'webtag']
