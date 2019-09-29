from flask import Flask, abort, request
import json

app = Flask(__name__)


@app.route('/foo', methods=['POST'])
def foo():
    if not request.json:
        abort(400)
    print(request.json)
    return json.dumps(request.json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1509, debug=True)
