import random
import re
from typing import List


class Encoder:
    def __init__(self, text: str):
        self.__encoded_text: str = self.__encode_text(text)

    @property
    def encoded_text(self) -> str:
        return self.__encoded_text

    def __encode_text(self, text: str, separator='\n—weird—\n', words_tokenizer=re.compile(r'(\w+)', re.U)) -> str:
        text_words: List[str] = words_tokenizer.findall(text)
        encoded_text_words: List[str] = [self.__encode_word(word) for word in text_words]
        sorted_text_words: List[str] = sorted(
            list(filter(lambda x: x not in encoded_text_words, text_words)),
            key=lambda s: s.casefold()
        )
        for word, encoded_word in zip(text_words, encoded_text_words):
            text = text.replace(word, encoded_word)

        return f'{separator}{text}{separator}{" ".join(sorted_text_words)}'

    def __encode_word(self, word: str) -> str:
        if word.__len__() > 4:
            chars = list(word[1:-1])
            random.shuffle(chars)
            return f'{word[0]}{"".join(chars)}{word[-1]}'  # randomly shuffle the mid letters instead of first and last one
        elif word.__len__() == 4:
            return f'{word[0]}{word[2:0:-1]}{word[3]}'  # for word where len == 4 we only shuffle two mid letters
        else:
            return word  # if the word consisted of less than 4 chars there is no need to shuffle it
