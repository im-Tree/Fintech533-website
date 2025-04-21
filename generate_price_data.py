import yfinance as yf
import pandas as pd
import json
import os

tickers = ["AAPL", "MSFT", "JPM", "XOM", "JNJ", "PG", "NVDA", "CAT", "HD", "AMZN"]

price_data = {}

for ticker in tickers:
    print(f"⏳ Fetching {ticker}...")
    df = yf.download(ticker, period="1mo", interval="1d", auto_adjust=True)

    # 确保索引重置，并手动提取列，强制重命名（避免 MultiIndex）
    df = df.reset_index()
    df = df[["Date", "Close"]]
    df.columns = ["Date", "Close"]
    df["Date"] = df["Date"].astype(str)
    df["Close"] = df["Close"].astype(float)

    price_data[str(ticker)] = df.to_dict(orient="records")

js_content = "const priceData = " + json.dumps(price_data) + ";"

os.makedirs("static", exist_ok=True)
with open("static/price_data.js", "w") as f:
    f.write(js_content)

print("✅ 成功生成 static/price_data.js")
