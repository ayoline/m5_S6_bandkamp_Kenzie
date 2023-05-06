from django.test import TestCase
from model_bakery import baker
from rest_framework.test import APITestCase


class SongsCreateTestView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.musician = baker.make('musicians.Musician')
        cls.album = baker.make('albums.Album', musician=cls.musician)

    def test_if_song_can_be_created(self):
        """
        Verifica se uma musica pode ser criada
        """
        new_song = {
            "name": "musica teste",
            "duration": 999
        }

        res = self.client.post(f"/api/musicians/{self.musician.id}/albums/{self.album.id}/songs/", new_song)

        self.assertEqual(201, res.status_code)


class SongListTestView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.musician = baker.make('musicians.Musician')
        cls.album = baker.make('albums.Album', musician=cls.musician)
        cls.song = baker.make('songs.Song', album=cls.album)

    def test_if_song_can_be_list(self):
        """
        Verifica se um som pode ser listado
        """
        res = self.client.get(f"/api/musicians/{self.musician.id}/albums/{self.album.id}/songs/")
        self.assertEqual(200, res.status_code)
