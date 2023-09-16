import datetime as dt
import matplotlib.pyplot as plt 
import yfinance as yf
from enum import Enum

class order(Enum):
    BUY = 1
    SELL = -1
    HOLD = 0

plt.style.use("dark_background")

ma_1 = 50
ma_2 = 200

start = dt.datetime.now() - dt.timedelta(days = 365*5)
end = dt.datetime.now()

stock_ticker = 'AAPL'

data = yf.download(stock_ticker,start , end)
#print (data)
data[f'SMA_{ma_1}'] = data['Adj Close'].rolling(window = ma_1).mean()
data[f'SMA_{ma_2}'] = data['Adj Close'].rolling(window = ma_2).mean()

data = data.iloc[ma_2:]
# plt.plot(data['Adj Close'], label = "Share Price" , color = "white")
# plt.plot(data[f'SMA_{ma_1}'],label = f"SMA {ma_1}",color = "red")
# plt.plot(data[f'SMA_{ma_2}'],label = f"SMA {ma_2}",color = "blue")
# plt.legend(loc = "upper left")
# plt.show()

buy_signals = []
sell_signals = []
trigger = order.HOLD

for x in range(len(data)):
    if data[f'SMA_{ma_1}'].iloc[x] > data[f'SMA_{ma_2}'].iloc[x] and trigger != order.BUY :
        buy_signals.append(data['Adj Close'].iloc[x])
        sell_signals.append(float('nan'))
        trigger = order.BUY
    elif data[f'SMA_{ma_1}'].iloc[x] < data[f'SMA_{ma_2}'].iloc[x] and trigger != order.SELL :
        buy_signals.append(float('nan'))
        sell_signals.append(data['Adj Close'].iloc[x])
        trigger = order.SELL
    else:
        buy_signals.append(float('nan'))
        sell_signals.append(float('nan'))

data['Buy Signals'] = buy_signals
data['Sell Signals'] = sell_signals

print(data)

plt.plot(data['Adj Close'], label = "Share Price" , alpha = 0.5)
plt.plot(data[f'SMA_{ma_1}'],label = f"SMA {ma_1}",color = "red",linestyle = "--")
plt.plot(data[f'SMA_{ma_2}'],label = f"SMA {ma_2}",color = "blue",linestyle = "--")
plt.scatter(data.index,data['Buy Signals'],label = "Buy Signal", marker="^", color = "green", lw= 3)
plt.scatter(data.index,data['Sell Signals'],label = "Sell Signal", marker="v", color = "red", lw= 3)
plt.legend(loc = "upper left")
plt.show()