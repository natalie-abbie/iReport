from flask import Flask, json, jsonify, request, Blueprint
from views.users import user
from views.redflag import flags

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(flags)


if __name__ == '__main__':
    app.run(debug=False)
