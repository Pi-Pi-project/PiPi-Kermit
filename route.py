from flask import Flask, request, jsonify
from flask_cors import CORS
from train import model_train
from predict import model_predict
import pymysql
from DB_connect_setting import DB

cursor = DB.cursor(pymysql.cursors.DictCursor)
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route("/input", methods=['POST'])
def input():
    email = request.json['email']
    model_train(email)

    return "end"

@app.route("/output", methods=['POST'])
def output():
    email = request.json['email']

    out = model_predict(email)

    return jsonify(out)

if __name__ == "__main__":
    app.run(host='0.0.0.0')