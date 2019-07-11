import re
from typing import List
from common.exceptions import WrongTextFormatException


class Decoder:
    separator_text = "weird"
    separator: str = f"\n—{separator_text}—\n"

    def __init__(self, text: str):
        self.__decoded_text: str = self.__decode_text(self.__validate_text_format(text))

    @property
    def decoded_text(self) -> str:
        return self.__decoded_text

    def __validate_text_format(self, text: str):
        if text.count(self.separator) != 2:
            raise WrongTextFormatException
        return text

    def __decode_text(self, encoded_text: str, tokenizer=re.compile(r'(\w+)', re.U)) -> str:
        encoded_text_words: List[str] = tokenizer.findall(encoded_text)
        encoded_words: List[str] = self.__get_encoded_words(encoded_text_words)
        original_words: List[str] = self.__get_original_words(encoded_text_words, encoded_words)

        for word in original_words:
            corresponding_encoded_word: str = self.__get_corresponding_encoded_word(word, encoded_words)
            encoded_text = encoded_text.replace(corresponding_encoded_word, word)

        return self.__unpack_original_text(encoded_text)

    def __get_encoded_words(self, encoded_text_words: List[str]) -> List[str]:
        # Return list of encoded words between -weird- separators
        weird = 0
        encoded_words = []
        for word in encoded_text_words:
            if word == self.separator_text:
                weird += 1
                if weird == 2:
                    break
            elif word:
                encoded_words.append(word)
        return encoded_words

    def __get_original_words(self, encoded_text_words: List[str], encoded_words: List[str]) -> List[str]:
        # Return list of words that has been encoded
        return list(filter(lambda word: word != self.separator_text and word not in encoded_words, encoded_text_words))

    def __get_corresponding_encoded_word(self, word: str, encoded_words: List[str]) -> str:
        # Filter encoded words list to find corresponding word which has the same length and the same first and last letters
        return \
            list(filter(lambda x: len(x) == word.__len__() and x[0] == word[0] and x[-1] == word[-1], encoded_words))[0]

    def __unpack_original_text(self, text: str) -> str:
        return text.rpartition(f"{self.separator}")[0].replace(f"{self.separator}", '')
