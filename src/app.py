from flask import Flask, jsonify
from flask_cors import CORS
from config import config

from routes import Chevrolet


app = Flask(__name__)
CORS(app, resources={"*": {"origins": "http://localhost:8080"}})

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(Chevrolet.main, url_prefix='/api/chevrolet')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()