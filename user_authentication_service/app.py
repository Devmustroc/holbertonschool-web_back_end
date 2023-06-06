from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """ GET /
    Return:
      - welcome message
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == '__main__':
    app.run()
