from celery import Celery, shared_task
from characters.scraper import sync_characters_with_api
from characters.models import Character

app = Celery('tasks', backend="redis://localhost:6379", broker='redis://localhost')

@shared_task
def run_sync_with_api() -> None:
    return sync_characters_with_api()