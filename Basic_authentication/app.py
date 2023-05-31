from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)