from albums.models import Album
from songs.models import Song
from albums.serializers import AlbumSerializer
from songs.serializers import SongSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)
from .models import Musician
from .serializers import MusicianSerializer
from django_filters import rest_framework as filters
from .paginations import CustomPagination


class SongFilter(filters.FilterSet):
    max_duration = filters.NumberFilter(field_name="duration", lookup_expr="lte")
    min_duration = filters.NumberFilter(field_name="duration", lookup_expr="gte")
    # favorite_language = filters.CharFilter(
    #     field_name="favorite_language", lookup_expr="icontains"
    # )

    class Meta:
        model = Song
        fields = ["name"]


class MusicianView(ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    pagination_class = CustomPagination


class MusicianDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    pagination_class = CustomPagination
    lookup_url_kwarg = "musician_id"


class MusicianAlbumView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        musician_id = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        albums = Album.objects.filter(musician=musician_id)
        return albums

    def perform_create(self, serializer):
        musician_id = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        serializer.save(musician=musician_id)


class MusicianAlbumSongView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SongFilter

    def get_queryset(self):
        musician_id = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        album_id = Album.objects.filter(
            id=self.kwargs["album_id"], musician=musician_id
        ).first()
        # album_id = get_object_or_404(Album, pk=self.kwargs["album_id"])
        # ipdb.set_trace()
        songs = Song.objects.filter(album=album_id)
        return songs

    def perform_create(self, serializer):
        musician_id = get_object_or_404(Musician, pk=self.kwargs["musician_id"])
        album = Album.objects.filter(musician=musician_id)
        album_id = get_object_or_404(album, pk=self.kwargs["album_id"])
        serializer.save(album=album_id)
