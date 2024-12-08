from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Merhaba! Flask uygulamanız çalışıyor."

@app.route('/api/signal')
def signal():
    return jsonify({
        "buy": "BTC",
        "sell": "ETH",
        "timestamp": "2024-12-08"
    })

if __name__ == '__main__':
    app.run(debug=True)
