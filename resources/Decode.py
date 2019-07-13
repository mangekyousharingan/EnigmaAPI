from flask_restful import Resource
from flask import jsonify
from common.decoder import Decoder
from common.parser import Parser


class Decode(Resource):

    @Parser.validate_attributes
    def put(self):
        text = Parser.attributes['text']
        decoded_text = Decoder.decode_text(text)
        return jsonify({'decoded_text': decoded_text})
