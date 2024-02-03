from collections import deque
from collections import defaultdict
from typing import List, Set


def find_sequence(
    start_word: str,
    end_word: str,
    words: Set[str],
    neighbours: defaultdict[str, List[str]],
) -> List[str]:
    """
    Finds a sequence of words from start_word to end_word, each differing by one letter.

    Parameters:
    start_word (str): Starting word of the sequence.
    end_word (str): Ending word of the sequence.
    words (Set[str]): Set of all possible words.
    neighbours (defaultdict[str, List[str]]): Dictionary mapping wildcard words to matching words.

    Returns:
    list: Sequence from start_word to end_word, or empty list if no sequence exists.
    """

    if start_word not in words or end_word not in words:
        return []

    if start_word == end_word:
        return [start_word]

    # Create a queue for BFS and enqueue the start word
    queue = deque([(start_word, [start_word])])

    # Create a set to keep track of visited words
    visited = set([start_word])

    while queue:
        current_word, path = queue.popleft()

        if current_word == end_word:
            return path

        # For each possible one-letter transformation of the current word
        for i in range(len(current_word)):
            wildcard_word = current_word[:i] + "*" + current_word[i + 1 :]

            for word in neighbours[wildcard_word]:
                if word not in visited:
                    queue.append((word, path + [word]))
                    visited.add(word)

    return []


def generate_neighbours(words):
    """
    Generates a dictionary mapping wildcard words to matching words. Used only during testing.

    A wildcard word is created by replacing each letter of the word with a wildcard.

    Parameters:
    words (Iterable[str]): An iterable of words.

    Returns:
    defaultdict[str, List[str]]: A dictionary where the keys are wildcard words and the values are lists of words that match the wildcard.
    """

    neighbors = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            wildcard_word = word[:i] + "*" + word[i + 1 :]
            neighbors[wildcard_word].append(word)
    return neighbors
