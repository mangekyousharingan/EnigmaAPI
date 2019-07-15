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
