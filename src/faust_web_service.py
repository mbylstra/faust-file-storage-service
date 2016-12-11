import os
from os.path import join
import json

from flask import make_response, request
from flask_restful import Resource
from flask import current_app


class StoreDspFile(Resource):

    def post(self):

        config = current_app.config
        username = request.args.get('username')
        filename = request.args.get('filename')
        source_code = request.data

        dir = join(config['GENERATED_STATIC_DIR'], username)
        file_path = join(dir, filename)
        try:
            os.makedirs(dir)
        except OSError:
            pass
        with open(file_path, mode='w') as f:
            f.write(source_code)




