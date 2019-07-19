"""
This module contains Decoder class with all methods to decode text to it's original value.
"""
import re
from typing import List
from common.exceptions import WrongTextFormatException


class Decoder:
    separator_text: str = "weird"
    separator: str = f"\n—{separator_text}—\n"
    words_tokenizer = re.compile(r'(\w+)', re.U)

    @classmethod
    def decode_text(cls, encoded_text: str) -> str:
        text_words = cls.words_tokenizer.findall(cls._validate_text_format(encoded_text))
        encoded_words = cls._get_encoded_words(text_words)
        original_words = cls._get_original_words(text_words, encoded_words)
        decoded_text = cls._replace_encoded_words_with_original(
            encoded_text, encoded_words, original_words
        )

        return cls._unpack_original_text(decoded_text)

    @staticmethod
    def _validate_text_format(text: str):
        if text.count(Decoder.separator) != 2:
            raise WrongTextFormatException
        return text

    @staticmethod
    def _get_encoded_words(text_words: List[str]) -> List[str]:
        """Return list of encoded words. All words between -weird- separators."""
        weird = 0
        encoded_words = []
        for word in text_words:
            if word == Decoder.separator_text:
                weird += 1
                if weird == 2:
                    break
            elif word:
                encoded_words.append(word)
        return encoded_words

    @staticmethod
    def _get_original_words(text_words: List[str], encoded_words: List[str]) -> List[str]:
        """Return list of words that has been encoded. Words after second separator."""
        return [word for word in text_words if word != Decoder.separator_text and word not in encoded_words]

    @staticmethod
    def _replace_encoded_words_with_original(encoded_text, encoded_words, original_words):
        text_with_originals = encoded_text
        for word in original_words:
            corresponding_encoded_word = Decoder._get_corresponding_encoded_word(word, encoded_words)
            text_with_originals = text_with_originals.replace(corresponding_encoded_word, word)
        return text_with_originals

    @staticmethod
    def _get_corresponding_encoded_word(word: str, encoded_words_list: List[str]) -> str:
        """Filter encoded words list to find corresponding words
        which has the same length, the same first and last letters
        and all the letters match between the words"""

        def first_and_last_letters_match(encoded_word, word) -> bool:
            return encoded_word[0] == word[0] and encoded_word[-1] == word[-1]

        def mid_letters_are_common(encoded_word, word):
            return sorted(encoded_word[1: -1]) == sorted(word[1: -1])

        return [encoded_word for encoded_word in encoded_words_list
                if first_and_last_letters_match(encoded_word, word)
                and mid_letters_are_common(encoded_word, word)][0]

    @staticmethod
    def _unpack_original_text(text: str) -> str:
        """Extracting original version of text. Updated text between separators."""
        return text.rpartition(f"{Decoder.separator}")[0].replace(f"{Decoder.separator}", '')
