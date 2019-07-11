from flask import Flask
from flask_restful import Api
from resources.Encode import Encode
from resources.Decode import Decode

errors = {
    'WrongTextFormatException': {
        'message': 'Wrong text format!',
        'status': 400,
        'extra': 'Please make sure that text is provided with proper format'
    }
}

app = Flask(__name__)
api = Api(app, catch_all_404s=True, errors=errors)

api.add_resource(Encode, '/v1/encode')
api.add_resource(Decode, '/v1/decode')

if __name__ == '__main__':
    app.run()
