from .settings import *

# Override the TESTING setting
TESTING = True
WORDS_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "api", "data", "test_words.txt")
