from django.urls import path

from characters.views import get_random_character_view, CharacterListView

app_name = "app"

urlpatterns = [
    path("characters/random/", get_random_character_view, name="character_random"),
    path("characters/", CharacterListView.as_view(), name="character_list"),
]
