from collections import deque
from collections import defaultdict
from typing import List, Set


def find_sequence(start_word: str, end_word: str, words: Set[str] , neighbours: defaultdict[str, List[str]] ):
    # Create a dictionary where the keys are words with one letter replaced by a wildcard
    # and the values are lists of words that match the key
    if start_word not in words or end_word not in words:
        return []

    if start_word == end_word:
        return [start_word]

    # Create a queue for BFS and enqueue the start word
    queue = deque([(start_word, [start_word])])

    # Create a set to keep track of visited words
    visited = set([start_word])

    while queue:
        # Dequeue a word from the queue
        current_word, path = queue.popleft()

        # If the current word is the end word, return the path
        if current_word == end_word:
            return path

        # For each possible one-letter transformation of the current word
        for i in range(len(current_word)):
            wildcard_word = current_word[:i] + "*" + current_word[i + 1 :]

            # If the wildcard_word is not in neighbours, skip to the next iteration
            if wildcard_word not in neighbours:
                continue

            # For each word that matches the transformation
            for word in neighbours[wildcard_word]:
                # If the word has not been visited
                if word not in visited:
                    # Enqueue the word and the path to it
                    queue.append((word, path + [word]))
                    # Mark the word as visited
                    visited.add(word)

    # If no path was found, return an empty list
    return []


def generate_neighbours(words):
    neighbors = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            wildcard_word = word[:i] + "*" + word[i + 1 :]
            neighbors[wildcard_word].append(word)
    return neighbors
