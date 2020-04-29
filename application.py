from flask import Flask
from flask import Flask,request,jsonify
import pandas as pd
import os
from flask_cors import CORS, cross_origin
path = os.getcwd()
app = Flask(__name__)
path = os.getcwd()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/assurent', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def TradeIn():  
        tradeInOptions = pd.read_csv("TradeOptions.csv")
        tradeIn = tradeInOptions["TradeOptions"]  
        tradeInList = [x for x in tradeIn if str(x) != 'nan']
        return "tradeInList"
