from flask import Flask, json, jsonify, request, Blueprint
from main.views.users import user
from main.views.redflag import flags

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(flags)


if __name__ == '__main__':
    app.run(debug=True)
