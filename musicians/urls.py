from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from . import views

urlpatterns = [
    path("musicians/", views.MusicianView.as_view()),
    path("musicians/<musician_id>/", views.MusicianDetailView.as_view()),
    path("musicians/<musician_id>/albums/", views.MusicianAlbumView.as_view()),
    path(
        "musicians/<musician_id>/albums/<album_id>/songs/",
        views.MusicianAlbumSongView.as_view(),
    ),
    # Acessa o download do schema
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Opcionais
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
