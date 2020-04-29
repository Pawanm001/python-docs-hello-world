from flask import Flask
from flask import Flask,request,jsonify
import pandas as pd
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/assurent', methods=['POST'])
def TradeIn():  
        text_data = request.form.get("data")
        tradeInOptions = pd.read_csv("TradeOptions.csv")
        tradeIn = tradeInOptions["TradeOptions"]  
        tradeInList = [x for x in tradeIn if str(x) != 'nan']
        return jsonify(tradeInList)
