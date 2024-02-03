from django.apps import AppConfig
from .word_loader import WordLoader


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        WordLoader.load_words()
