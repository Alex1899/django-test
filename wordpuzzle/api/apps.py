import time
from django.apps import AppConfig
from halo import Halo
from .word_loader import WordLoader


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        start_time = time.time()
        spinner = Halo(text="Loading dictionary words...", spinner="dots")
        spinner.start()

        try:
            WordLoader.load_words()

            end_time = time.time()
            total_time = end_time - start_time

            spinner.stop_and_persist(
                symbol="✅".encode("utf-8"),
                text=f"Loaded words in {round(total_time, 1)} seconds",
            )

        except Exception as e:
            spinner.stop_and_persist(
                symbol="❌".encode("utf-8"), text=f"Error while loading words: {e}"
            )
