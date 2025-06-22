import yfinance as yf
from sklearn.linear_model import LinearRegression
import numpy as np

def get_stock_prediction(symbol):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="6mo")

    if hist.empty:
        raise Exception("No stock data found.")

    hist = hist.reset_index()
    hist['Days'] = np.arange(len(hist))

    X = hist[['Days']]
    y = hist['Close']

    model = LinearRegression()
    model.fit(X, y)

    # Predict next day
    next_day = np.array([[len(hist)]])
    predicted_price = model.predict(next_day)[0]
    return predicted_price
