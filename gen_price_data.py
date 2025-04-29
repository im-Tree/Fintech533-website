# save as gen_price_data.py，和 static/ledger.csv 同级
import pandas as pd, json

# ① 读 CSV
df = pd.read_csv("static/ledger.csv", parse_dates=["Date"])

# ② 把日期格式化成字符串列表，把数值列表化
dates  = df["Date"].dt.strftime("%Y-%m-%d").tolist()
values = df["Market Value"].tolist()

# ③ 拼成一个 JS trace 对象
js = f"""
var portfolioTrace = {{
  x: {json.dumps(dates)},
  y: {json.dumps(values)},
  type: 'scatter',
  mode: 'lines',
  name: 'Portfolio Market Value'
}};
"""

# ④ 写入 static/price_data.js
with open("static/price_data.js", "w", encoding="utf-8") as f:
    f.write(js)
print("Wrote static/price_data.js")
