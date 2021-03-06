import os
import util
import db
from flask import Flask, json, url_for, redirect #requests
from flask_cors import CORS
from flask_restful import Api
from resources.userHistory import UserHistory
from dotenv import load_dotenv

# Load Environment variables
load_dotenv()

app = Flask(__name__)
# Allow cross domain apps to access API
CORS(app)

# Provide Mongo Atlas URI, stored in config file
app.config["MONGO_URI"] = os.getenv("MONGO_URI_MASTER")
# Set custom JSON Encoder for Mongo Object
app.json_encoder = util.MongoEncoder
db.mongo.init_app(app)
api = Api(app)

api.add_resource(UserHistory, "/userhistory")

# Vanilla Flask route
@app.route("/", methods=["GET"])
def index():
    return "Backend for SmallBusinesses"

@app.route("/doaprogram/<id>", methods=["GET"])
def doaprogram(id):
    print("a program has run")
    return redirect(url_for('index'))



# Handles validation errors and returns JSON Object
@app.errorhandler(422)
@app.errorhandler(400)
def handle_error(err):
    messages = err.data.get("messages", ["Invalid request."])
    return json.jsonify({"errors": messages}), err.code


if __name__ == "__main__":
    app.run(debug=True)
