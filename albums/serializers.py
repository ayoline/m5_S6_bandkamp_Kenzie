# from musicians.serializers import MusicianSerializer
from rest_framework import serializers
from .models import Album
from songs.models import Song


class AlbumSerializer(serializers.ModelSerializer):
    songs_count = serializers.SerializerMethodField()
    total_duration = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = [
            "id",
            "name",
            "musician_id",
            "songs_count",
            "total_duration",
        ]
        read_only_fields = ["musician_id"]

    def get_songs_count(self, obj: Album):
        musics_obj = Song.objects.filter(album=obj)
        return len(musics_obj)

    def get_total_duration(elf, obj: Album):
        musics_obj = Song.objects.filter(album=obj)
        seconds = 0

        for music in musics_obj:
            seconds += music.duration

        return seconds
