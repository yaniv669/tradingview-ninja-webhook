from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "OK", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return "No data", 400
    action = data.get("action", "").upper()
    quantity = data.get("quantity", 1)
    symbol = data.get("symbol", "NQ 06-26")
    account = data.get("account", "Sim101")
    order = f"PLACE;account={account};instrument={symbol};action={action};qty={quantity};orderType=MARKET\n"
    with open("/tmp/order.txt", "w") as f:
        f.write(order)
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
