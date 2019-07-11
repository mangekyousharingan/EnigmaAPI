from functools import wraps
from typing import Dict

from flask_restful import reqparse


class Parser:

    attributes: Dict[str, str]

    def __init__(self):
        self.__request_parser = reqparse.RequestParser()
        self.__request_parser.add_argument(
            'text',
            location='json',
            type=str,
            help='Text must be provided!',
            required=True
        )

    @property
    def request_parser(self):
        return self.__request_parser

    @staticmethod
    def validate_attributes(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            parser = Parser()
            Parser.attributes = parser.request_parser.parse_args()

            return func(*args, **kwargs)
        return decorator


