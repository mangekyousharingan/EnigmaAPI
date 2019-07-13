import random
import re
from typing import List


class Encoder:
    
    @classmethod
    def encode_text(cls, text: str, separator='\n—weird—\n', words_tokenizer=re.compile(r'(\w+)', re.U)) -> str:
        text_words: List[str] = list(filter(lambda word: len(word) >= 4, words_tokenizer.findall(text)))
        encoded_text_words: List[str] = [cls._encode_word(word) for word in text_words]
        sorted_text_words: List[str] = sorted(
            list(filter(lambda x: x not in encoded_text_words, text_words)),
            key=lambda s: s.casefold()
        )
        encoded_text = cls._replace_words_by_encoded_words_in_text(text, text_words, encoded_text_words)

        return f'{separator}{encoded_text}{separator}{" ".join(sorted_text_words)}'

    @staticmethod
    def _encode_word(word: str) -> str:
        if word.__len__() > 4:
            chars = list(word[1:-1])
            random.shuffle(chars)
            return f'{word[0]}{"".join(chars)}{word[-1]}'  # randomly shuffle  mid letters instead of first and last one
        else:
            return f'{word[0]}{word[2:0:-1]}{word[3]}'  # for word where len == 4 we only shuffle two mid letters

    @staticmethod
    def _replace_words_by_encoded_words_in_text(text: str, text_words: List[str],
                                                encoded_words: List[str]) -> str:
        updated_text = text

        for word, encoded_word in zip(text_words, encoded_words):
            updated_text = updated_text.replace(word, encoded_word)

        return updated_text
