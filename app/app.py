from flask import Flask, json, jsonify, request, Blueprint
from users import user
from redflag import flags

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(flags)


if __name__ == '__main__':
    app.run(debug=True)