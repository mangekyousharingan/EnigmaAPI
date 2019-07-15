import unittest
from common.decoder import Decoder
from common.exceptions import WrongTextFormatException


class TestDecoder(unittest.TestCase):
    def setUp(self):
        self.separator = '\n—weird—\n'

    def test_Decoder_if_exception_raised_when_format_is_incorrect(self):
        text = "This is text without separatorts."
        self.assertRaises(WrongTextFormatException, lambda: Decoder.decode_text(text))

    def test_Decoder_when_empty_text_given(self):
        text = f'{self.separator}{self.separator}'
        self.assertEqual("", Decoder.decode_text(text))

    def test_Decoder_if_text_decoded_properly(self):
        encoded_text = "\n—weird—\nSmoe emxplae txet\n—weird—\nexample Some text"
        decoded_text = Decoder.decode_text(encoded_text)
        self.assertEqual("Some example text", decoded_text)

    def test_if_get_encoded_words_return_all_words_between_separators(self):
        text_words = ['weird', 'Tihs', 'is', 'a', 'lnog', 'loonog', 'tset', 'stcennee', 'weird',
                      'long', 'looong', 'sentence', 'test', 'This']

        encoded_words = Decoder._get_encoded_words(text_words)
        expected_output = ['Tihs', 'is', 'a', 'lnog', 'loonog', 'tset', 'stcennee']
        self.assertTrue(all(word in encoded_words for word in expected_output))

    def test_if_get_original_words_returns_all_encoded_words(self):
        text_words = ['weird', 'Tihs', 'is', 'a', 'lnog', 'loonog', 'tset', 'stcennee', 'weird',
                      'long', 'looong', 'sentence', 'test', 'This']
        encoded_words = ['Tihs', 'is', 'a', 'lnog', 'loonog', 'tset', 'stcennee']
        expected_output = ['long', 'looong', 'sentence', 'test', 'This']
        original_words = Decoder._get_original_words(text_words, encoded_words)
        self.assertTrue(all(word in expected_output for word in original_words))

    def test_replace_encoded_words_with_originals(self):
        encoded_text = '\n—weird—\nSmoe emxplae txet\n—weird—\nexample Some text'
        encoded_words = ['Smoe', 'emxplae', 'txet']
        original_words = ['example', 'Some', 'text']
        expected_output = '\n—weird—\nSome example text\n—weird—\nexample Some text'
        text_with_originals = Decoder._replace_encoded_words_with_original(
            encoded_text, encoded_words, original_words
        )
        self.assertEqual(text_with_originals, expected_output)

    def test_if_get_coressponding_encoded_words_returns_proper_word_for_given_one(self):
        word = "testWord"
        encoded_words = ["test", "testord", "testWor", "tWorestd"]
        corresponding_word = Decoder._get_corresponding_encoded_word(word, encoded_words)
        self.assertEqual("tWorestd", corresponding_word)

    def test_if_unpack_original_text_returns_original_version_of_text(self):
        text = '\n—weird—\nSome example text\n—weird—\nexample Some text'
        original = 'Some example text'
        unpacked_txt = Decoder._unpack_original_text(text)
        self.assertEqual(unpacked_txt, original)
