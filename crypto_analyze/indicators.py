import ta

def indicators(data): 
    #RSI indicator
    rsi = ta.momentum.RSIIndicator(data['Close'].squeeze(), window=14)
    data['RSI'] = rsi.rsi()

    #ATR indicator
    atr = ta.volatility.AverageTrueRange(data['High'].squeeze(), data['Low'].squeeze(), data['Close'].squeeze(), window=14, fillna=True).average_true_range()
    data['ATR'] = atr

    #EMA50 and EMA200 indicator
    ema50 = ta.trend.EMAIndicator(data['Close'].squeeze(), window=50, fillna=False)
    ema200 = ta.trend.EMAIndicator(data['Close'].squeeze(), window=200, fillna=False)
    data['EMA50'] = ema50.ema_indicator()
    data['EMA200'] = ema200.ema_indicator()

    data["ema_cross_up"] = (data["EMA50"] > data["EMA200"]) & (data["EMA50"].shift(1) <= data["EMA200"].shift(1))
    data["ema_cross_down"] = (data["EMA50"] < data["EMA200"]) & (data["EMA50"].shift(1) >= data["EMA200"].shift(1))

    #OBV indicator
    obv = ta.volume.OnBalanceVolumeIndicator(close=data['Close'].squeeze(), volume=data['Volume'].squeeze()).on_balance_volume()
    data['OBV'] = obv
    data['OBV_SMA'] = data['OBV'].rolling(window=20).mean()

    data['OBV_SMA_cross_up'] = (data['OBV_SMA'] > data['OBV']) & (data['OBV_SMA'].shift(1) <= data['OBV'].shift(1))
    data['OBV_SMA_cross_down'] = (data['OBV_SMA'] < data['OBV']) & (data['OBV_SMA'].shift(1) >= data['OBV'].shift(1))
    return data

