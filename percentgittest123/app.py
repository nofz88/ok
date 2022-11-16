from flask import Flask, request
from telegram import telegram_bot2
from telegram import telegram_bot1

app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def index():
    return "Hello World!"



@app.route("/percent", methods=["GET", "POST"])
def tradingview1():
    data1 = request.data
    symbol = str(json_data["symbol"])
    price = str(json_data["price"])
    message = symbol + ": " + price
    
    telegram_bot1(data1.decode())
    return data1.decode()
    
@app.route("/ema", methods=["GET", "POST"])
def tradingview2():
    data2 = request.data
    symbol = str(json_data["symbol"])
    price = str(json_data["price"])
    message = symbol + ": " + price
    
    telegram_bot2(data2.decode())
    return data2.decode()



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)