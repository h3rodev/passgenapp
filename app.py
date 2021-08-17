from flask import Flask, jsonify
from flask_cors import CORS
import genPass

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/api/gen/<int:c>', methods=['GET'])
def ping_pong(c):
    passgen = {
        "data": genPass.genPass(c)
    }

    return jsonify(passgen)


if __name__ == '__main__':
    app.run()
