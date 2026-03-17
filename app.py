from flask import Flask, render_template_string, request, jsonify
import os

app = Flask(__name__)

# Security Token
API_TOKEN = os.environ.get("API_TOKEN", "fallback-secret")

# In-memory storage for latest state
state = {
    "portfolio": {"value": "10000", "pnl": "0", "btc": "0"},
    "market": {"price": "Waiting...", "rsi": "0", "regime": "SCANNING"},
    "logs": "System initialized. Waiting for first bot pulse..."
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Master Quant v3.0 | Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css">
    <style>
        body { background-color: #050505; color: #00ff41; font-family: 'Courier New', Courier, monospace; }
        .box { background-color: #0a0a0a; border: 1px solid #00ff41; color: #00ff41; border-radius: 0; }
        .title { color: #00ff41 !important; text-transform: uppercase; letter-spacing: 2px; }
        pre { background: #000; color: #00ff41; border: 1px solid #00ff41; border-radius: 0; white-space: pre-wrap; font-size: 0.85rem; }
        .glitch { animation: glitch 1s linear infinite; }
        @keyframes glitch { 2%, 64% { transform: translate(2px,0) skew(0deg); } 4%, 60% { transform: translate(-2px,0) skew(0deg); } 62% { transform: translate(0,0) skew(5deg); } }
        .stat-value { font-size: 1.5rem; font-weight: bold; }
    </style>
    <meta http-equiv="refresh" content="30">
</head>
<body class="p-6">
    <div class="container">
        <h1 class="title is-1 glitch">🧙‍♂️ Master Quant v3.0</h1>
        <hr style="background-color: #00ff41;">
        
        <div class="columns">
            <div class="column is-4">
                <div class="box">
                    <h2 class="title is-4">System Status</h2>
                    <p>Mode: [STRICT_PAPER]</p>
                    <p>Portfolio: <span class="stat-value">${{ state.portfolio.value }}</span></p>
                    <p>Unrealized PnL: <span class="stat-value" style="color: {% if state.portfolio.pnl|float >= 0 %}#00ff41{% else %}#ff0000{% endif %};">{{ state.portfolio.pnl }} USD</span></p>
                    <p>BTC Held: <span class="stat-value">{{ state.portfolio.btc }}</span></p>
                </div>
            </div>
            <div class="column is-8">
                <div class="box">
                    <h2 class="title is-4">Trading Signals</h2>
                    <p>Regime: <span class="stat-value">[{{ state.market.regime }}]</span></p>
                    <p>BTC/USD Price: <span class="stat-value">${{ state.market.price }}</span></p>
                    <p>RSI (14): <span class="stat-value">{{ state.market.rsi }}</span></p>
                </div>
            </div>
        </div>

        <div class="box">
            <h2 class="title is-4">Terminal Output (Last Update)</h2>
            <pre>{{ state.logs }}</pre>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, state=state)

@app.route('/update', methods=['POST'])
def update():
    token = request.headers.get("Authorization")
    if token != f"Bearer {API_TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401
    
    data = request.json
    state["portfolio"] = data.get("portfolio", state["portfolio"])
    state["market"] = data.get("market", state["market"])
    state["logs"] = data.get("logs", state["logs"])
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
