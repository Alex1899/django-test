from django.test import TestCase
from collections import defaultdict
from django.urls import reverse
from .utils import find_sequence, generate_neighbours



# API endpoint test
class WordPuzzleApiTest(TestCase):
    def setUp(self):
        self.url = reverse("wordpuzzle")

    def test_get_success(self):
        """
        Test that the API returns a 200 status code and the correct sequence
        when given valid startWord and endWord parameters.
        """
        response = self.client.get(self.url, {"startWord": "hit", "endWord": "cog"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"sequence":["hit", "cit", "cot", "cog"]})

    def test_get_no_start_word(self):
        response = self.client.get(self.url, {"endWord": "cog"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"error": "Both 'startWord' and 'endWord' parameters are required"},
        )

    def test_get_no_end_word(self):
        response = self.client.get(self.url, {"startWord": "hit"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(),
            {"error": "Both 'startWord' and 'endWord' parameters are required"},
        )

    def test_get_start_word_not_in_dictionary(self):
        response = self.client.get(self.url, {"startWord": "yyy", "endWord": "cog"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"sequence": []})

    def test_get_end_word_not_in_dictionary(self):
        response = self.client.get(self.url, {"startWord": "hit", "endWord": "ghj"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"sequence": []})

    def test_get_no_possible_sequence(self):
        response = self.client.get(self.url, {"startWord": "hit", "endWord": "xyz"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"sequence": []})



# Algorithm test: find shortest sequence
class FindSequenceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.words = [
            "flour",
            "game",
            "stool",
            "bingo",
            "chair",
            "fleur",
            "flear",
            "blear",
            "bleak",
            "break",
            "bread",
        ]
        cls.neighbours = generate_neighbours(cls.words)

    def test_find_sequence(self):
        start_word = "flour"
        end_word = "bread"
        expected_output = [
            "flour",
            "fleur",
            "flear",
            "blear",
            "bleak",
            "break",
            "bread",
        ]
        self.assertEqual(
            find_sequence(start_word, end_word, self.words, self.neighbours),
            expected_output,
        )

    def test_no_path(self):
        start_word = "flour"
        end_word = "bingo"
        expected_output = []
        self.assertEqual(
            find_sequence(start_word, end_word, self.words, self.neighbours),
            expected_output,
        )

    def test_same_start_and_end_word(self):
        start_word = "flour"
        end_word = "flour"
        expected_output = ["flour"]
        self.assertEqual(
            find_sequence(start_word, end_word, self.words, self.neighbours),
            expected_output,
        )

    def test_different_length_words(self):
        start_word = "flour"
        end_word = "breaded"
        expected_output = []
        self.assertEqual(
            find_sequence(start_word, end_word, self.words, self.neighbours),
            expected_output,
        )

    def test_word_not_in_dictionary(self):
        start_word = "flour"
        end_word = "stone"
        expected_output = []
        self.assertEqual(
            find_sequence(start_word, end_word, self.words, self.neighbours),
            expected_output,
        )


# Utils test: generate_neighbours
class GenerateNeighboursTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.words = ["cat", "bat", "bet", "bot", "bop", "pop"]

    def test_generate_neighbours(self):
        expected_output = defaultdict(
            list,
            {
                "*at": ["cat", "bat"],
                "c*t": ["cat"],
                "ca*": ["cat"],
                "*at": ["cat", "bat"],
                "b*t": ["bat", "bet", "bot"],
                "ba*": ["bat"],
                "*et": ["bet"],
                "be*": ["bet"],
                "*ot": ["bot"],
                "bo*": ["bot", "bop"],
                "*op": ["bop", "pop"],
                "b*p": ["bop"],
                "p*p": ["pop"],
                "po*": ["pop"],
            },
        )
        self.assertEqual(generate_neighbours(self.words), expected_output)
