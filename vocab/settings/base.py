from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


DATA_DIR = BASE_DIR / 'data'
LANG_LEARNING_DICT_DIR = DATA_DIR / 'lang_learning_dict'
BOOK_DIR = DATA_DIR / 'book'
BASE_EBOOK_DIR = BASE_DIR / '..' / 'kindle'

FILTERED_SPECIAL_CHARS = [',', '.', '?', '!', '\'', '’', '‘', '-', '—', '–', '…', '\xa0', '(', ')', ';', '©', ':', '“', '”', '*', '«', '»', '¡', '¿', '·', '€', '™', '¨', '´', '¢', '§', '/', '®', '@', '‰', '‚', '\x9d', '#', '<', '>', '[', '"', ']', '$', '\\', '_', '=', '{', '}', '¦', '+', '%', '|', '&', '¬', '\u200b']