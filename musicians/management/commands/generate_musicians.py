from musicians.models import Musician
from albums.models import Album
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    help = "create 2 random user with 2 random albums"

    def handle(self, *args, **options):
        for i in range(2):
            musician_obj = {
                "first_name": get_random_string(5),
                "last_name": get_random_string(10),
                "instrument": "guitar",
            }

            musician = Musician.objects.create(**musician_obj)

            album_obj = {"name": get_random_string(5), "musician_id": musician.id}
            Album.objects.create(**album_obj)
