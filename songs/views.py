from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from songs import serializers
from songs.serializers import SongSerializer
from songs.models import Song


# function songs_list is going to accept GET and POST request
@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == 'GET':
        # query all the songs from database
        songs = Song.objects.all()
        # turn python data into JSON data via serializer
        serializers = SongSerializer(songs, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        # pass the new data into the serializer
        # request.data which can access the data on the incoming request
        serializers = SongSerializer(data=request.data)
        # # check whether the data is valid, it is not valide raise an error
        # else save it in the database
        # method 1
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)

        # method 2
        # if serializers.is_valid() == True:
        #     serializers.save()
        #     return Response(serializers.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def song_detail(request, pk):

    # search the song table and return song which its id/pk equals to pk
    # if the song exists in the database, return the song's info
    # if the song doesnt exist in the database, return status code 404

    # # method 1
    # try:
    #     song = Song.objects.get(id=pk)
    #     serializers = SongSerializer(song)
    #     return Response(serializers.data)
    # except Song.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    # # method 2
    song = get_object_or_404(Song, id=pk)
    serializer = SongSerializer(song)
    return Response(serializer.data)
