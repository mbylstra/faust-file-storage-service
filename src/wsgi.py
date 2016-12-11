import os
from envparse import env
from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS
import json

from faust_web_service import StoreDspFile

app = Flask(__name__)


print json.dumps(dict(os.environ), indent=2)

CONFIG_MODES = {
    'DEVELOPMENT': 'config.DevelopmentConfig',
    'PRODUCTION_DOCKER': 'config.ProductionDockerConfig',
}

config_mode = env('FLASK_CONFIG_MODE', default='DEVELOPMENT')
config_path = CONFIG_MODES[config_mode]
app.config.from_object(config_path)
print app.config

CORS(app)
api = Api(app)
api.add_resource(StoreDspFile, '/store-dsp-file')


if config_mode == 'DEVELOPMENT':
    @app.route('/gen-static/<path:filepath_end_part>')
    def serve_gen_static_file(filepath_end_part):
        print 'filepath end part', filepath_end_part
        return send_from_directory(
            app.config['GENERATED_STATIC_DIR'],
            filepath_end_part
        )


if __name__ == "__main__":
    app.run()
