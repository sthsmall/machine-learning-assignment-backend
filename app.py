from flask import Flask
from controller import all_blueprints
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

for blueprint in all_blueprints:
    app.register_blueprint(blueprint)


if __name__ == '__main__':
    app.run(debug=True)
