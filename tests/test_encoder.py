import unittest
from common.encoder import Encoder


class TestEncoder(unittest.TestCase):
    def setUp(self):
        self.separator = '\n—weird—\n'

    def test_Encoder_if_text_is_empty_string(self):
        text = ""
        list_of_encoded_words = ""
        encoded_text = Encoder.encode_text(text)
        expected_output = f"{self.separator}{text}{self.separator}{list_of_encoded_words}"
        self.assertEqual(encoded_text, expected_output)

    def test_Encoder_if_text_is_whitespace(self):
        text = " "
        list_of_encoded_words = ""
        encoded_text = Encoder.encode_text(text)
        expected_output = f"{self.separator}{text}{self.separator}{list_of_encoded_words}"
        self.assertEqual(encoded_text, expected_output)

    def test_encode_words_if_word_length_is_grater_than_4(self):
        word = "fourth"
        encoded_word = Encoder._encode_word(word)
        self.assertNotEqual(word, encoded_word)

    def test_encode_words_if_word_length_is_equal_than_4(self):
        word = "trio"
        expected_output = "tiro"
        encoded_word = Encoder._encode_word(word)
        self.assertEqual(expected_output, encoded_word)

    def test_replace_words_by_encoded_words_in_text(self):
        text = "some sample text"
        text_words = text.split(' ')
        encoded_words = ['encode_1', 'encode_2', 'encode_3']

        updated_text = Encoder._replace_words_by_encoded_words_in_text(text, text_words, encoded_words)
        expected_output = "encode_1 encode_2 encode_3"
        self.assertEqual(updated_text, expected_output)
