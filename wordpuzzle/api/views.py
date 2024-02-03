import time
import logging

from django.http import JsonResponse
from django.views import View
from .word_loader import WordLoader
from .utils import find_sequence

logger = logging.getLogger(__name__)

class WordPuzzleApi(View):
    """Implement the API here"""

    def get(self, request):
        """
        Handles GET requests to the word puzzle API.

        Parameters:
        - request (HttpRequest): The request object.
        - *args: Variable length argument list.
        - **kwargs: Arbitrary keyword arguments.

        Returns:
        - JsonResponse: A response with either the sequence of words or an error message.
        """

        start_word = request.GET.get("startWord")
        end_word = request.GET.get("endWord")

        if not start_word or not end_word:
            return JsonResponse(
                {"error": "Both 'startWord' and 'endWord' parameters are required"},
                status=400,
            )
        
        if not start_word.isalpha() or not end_word.isalpha():
            return JsonResponse(
                {"error": "'startWord' and 'endWord' must only contain alphabetic characters"},
                status=400,
            )

        if len(start_word) != len(end_word):
            return JsonResponse(
                {"error": "'startWord' and 'endWord' must be of the same length"},
                status=400,
            )



        start_time = time.time()
        words = WordLoader.get_word_set()
        neighbours = WordLoader.get_neighbors()
        sequence = find_sequence(start_word, end_word, words, neighbours)
        end_time = time.time()
        total_time = end_time - start_time
        logging.info(f"Total time taken to find sequence: {round(total_time * 1000, 2)} ms")

        if sequence:
            return JsonResponse({"sequence": sequence})
        else:
            return JsonResponse({"sequence": []})
