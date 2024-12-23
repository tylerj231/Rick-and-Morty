import requests

from characters.models import Character
from rick_and_morty_api import settings


def scrape_characters() -> list[Character]:
    next_url_to_scrape = settings.CHARACTERS_API_URL

    characters = []
    while next_url_to_scrape is not None:
        characters_response = requests.get(next_url_to_scrape).json()
        for character in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character["id"],
                    name=character["name"],
                    status=character["status"],
                    species=character["species"],
                    gender=character["gender"],
                    image=character["image"],
                )
        )
        next_url_to_scrape = characters_response["info"]["next"]
    return characters

def save_characters(characters: list[Character]):
    for character in characters:
        character.save()

def sync_characters_with_api() -> None:
    characters = scrape_characters()
    save_characters(characters)