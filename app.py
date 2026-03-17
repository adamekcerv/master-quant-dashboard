from flask import Flask, render_template_string
import os
import requests

app = Flask(__name__)

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
        .tag { border-radius: 0; font-weight: bold; }
        .is-profit { background-color: #003300; color: #00ff41; border: 1px solid #00ff41; }
        .is-loss { background-color: #330000; color: #ff0000; border: 1px solid #ff0000; }
        pre { background: #000; color: #00ff41; border: 1px solid #00ff41; border-radius: 0; }
        .glitch { animation: glitch 1s linear infinite; }
        @keyframes glitch { 2%, 64% { transform: translate(2px,0) skew(0deg); } 4%, 60% { transform: translate(-2px,0) skew(0deg); } 62% { transform: translate(0,0) skew(5deg); } }
    </style>
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
                    <p>Uptime: Active</p>
                    <p>Target: BTC/USD</p>
                </div>
            </div>
            <div class="column is-8">
                <div class="box">
                    <h2 class="title is-4">Trading Signals</h2>
                    <p>Regime: [TRENDING_BULL]</p>
                    <p>Score: 8/10</p>
                    <p>Logic: EMA12 > EMA26 > SMA50</p>
                </div>
            </div>
        </div>

        <div class="box">
            <h2 class="title is-4">Terminal Output</h2>
            <pre>
[2026-03-17 08:42] SYSTEM_INIT: Paper account initialized ($10,000)
[2026-03-17 08:43] ORDER_EXEC: BUY 0.01 BTC @ $74,428
[2026-03-17 08:50] MONITOR: Current PnL -1.94 USD
[2026-03-17 09:00] SCAN: Signal strength High (RSI 58)
            </pre>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
