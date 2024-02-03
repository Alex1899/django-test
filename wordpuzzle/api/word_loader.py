import time
from collections import defaultdict
from django.conf import settings
from halo import Halo


class WordLoader:
    """Class that provides an access to the dictionary"""

    words = set()
    neighbours = defaultdict(list)

    @classmethod
    def load_words(cls):
        """
        Loads words from "words.txt", populates 'words' set and 'neighbours' dictionary.

        For each word, it generates "wildcard words" by replacing each letter of the word with a "*",
        and maps these wildcard words to the original word in the neighbors dictionary. This is used to
        quickly find all words that can be formed by changing one letter of a given word.

        """

        start_time = time.time()
        # Start the loading spinner in a separate thread
        spinner = Halo(text="Loading dictionary words...", spinner="dots")
        spinner.start()

        try:
            start_time = time.time()

            with open(settings.WORDS_FILE_PATH, "r", encoding="utf-8") as file:
                for line in file:
                    word = line.strip()
                    cls.words.add(word)
                    for i in range(len(word)):
                        wildcard_word = word[:i] + "*" + word[i + 1 :]
                        cls.neighbours[wildcard_word].append(word)

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

    @classmethod
    def get_word_set(cls):
        return cls.words

    @classmethod
    def get_neighbors(cls):
        return cls.neighbours
