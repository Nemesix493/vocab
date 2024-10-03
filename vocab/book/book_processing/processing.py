from .parsing import ParsingBook


class ProcessingWordlist(dict):
    """
    This class manage the processing of wordlist
    """

    @staticmethod
    def lower_words(wordlist: list[str]) -> list[str]:
        """
        This method return the list of the undercase word  
        """
        return [
            word.lower()
            for word in wordlist
        ]

    @classmethod
    def process_words_occurences(cls, wordlist: list[str]) -> dict[str:int]:
        """
        This method process the number of occurence of each word
        """
        occurences = dict()
        for word in cls.lower_words(wordlist):
            if word in occurences.keys():
                occurences[word] += 1
            else:
                occurences[word] = 1
        return occurences
