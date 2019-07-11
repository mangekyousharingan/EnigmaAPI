from flask_restful import Resource
from flask import jsonify
from common.decoder import Decoder
from common.parser import Parser


class Decode(Resource):

    @Parser.validate_attributes
    def put(self):
        text = Parser.attributes['text']
        decoder = Decoder(text)

        return jsonify({'decoded_text': decoder.decoded_text})
