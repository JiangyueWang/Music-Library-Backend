from rest_framework import serializers
from songs.models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # each list item in the fields list represent the column from the Song model(table)
        # only the column listed in fields list can be visible to the user
        fields = ['id', 'title', 'artist', 'album', 'release_date', 'genre']
