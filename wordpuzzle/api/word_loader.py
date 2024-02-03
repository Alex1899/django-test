import os
from collections import defaultdict


class WordLoader:
    """Class that provides an access to the dictionary"""

    words = set()
    neighbors = defaultdict(list)

    @classmethod
    def load_words(cls):
        app_dir = os.path.dirname(__file__)
        with open(app_dir + "/data/words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                cls.words.add(word)
                for i in range(len(word)):
                    wildcard_word = word[:i] + "*" + word[i + 1 :]
                    cls.neighbors[wildcard_word].append(word)

    @classmethod
    def get_word_set(cls):
        return cls.words

    @classmethod
    def get_neighbors(cls):
        return cls.neighbors
