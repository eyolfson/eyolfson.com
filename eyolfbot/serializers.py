from rest_framework import serializers

from .models import Connection

class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Connection
        fields = ['utoronto_id', 'discord_id', 'gitlab_id']


