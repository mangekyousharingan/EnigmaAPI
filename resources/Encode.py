from flask_restful import Resource
from flask import jsonify
from common.encoder import Encoder
from common.parser import Parser


class Encode(Resource):

    @Parser.validate_attributes
    def put(self):
        text = Parser.attributes['text']
        encoder = Encoder(text)

        return jsonify({'encoded_text': encoder.encoded_text})
