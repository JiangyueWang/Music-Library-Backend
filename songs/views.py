from rest_framework.decorators import api_view
from rest_framework.response import Response
from songs.serializers import SongSerializer
from songs.models import Song


@api_view(['GET'])
def songs_list(request):
    # query all the songs from database
    songs = Song.objects.all()
    # turn python data into JSON data via serializer
    serializers = SongSerializer(songs, many=True)
    return Response(serializers.data)
