import os
from collections import defaultdict


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
        app_dir = os.path.dirname(__file__)
        with open(app_dir + "/data/words.txt", "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                cls.words.add(word)
                for i in range(len(word)):
                    wildcard_word = word[:i] + "*" + word[i + 1 :]
                    cls.neighbours[wildcard_word].append(word)

    @classmethod
    def get_word_set(cls):
        return cls.words

    @classmethod
    def get_neighbors(cls):
        return cls.neighbours
