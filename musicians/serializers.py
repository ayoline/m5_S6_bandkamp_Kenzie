from rest_framework import serializers
from .models import Musician
from albums.serializers import AlbumSerializer


class MusicianSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Musician
        fields = [
            "id",
            "first_name",
            "last_name",
            "instrument",
            "albums",
        ]
        read_only_fields = ["albums"]
