from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlist = serializers.HyperlinkedIdentityField(view_name='snippet-highlist', format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlist', 'title', 'code', 'lineos', 'language', 'style', 'owner']
