import pandas as pd

def detect_candlestick_patterns(df):
    signals = [None] * len(df)  # dopasuj długość sygnałów do df od początku
    categories = [None] * len(df)  # dodaj kategorię dla każdego wzorca
    
    # Define pattern categories
    bullish_patterns = {
        "Hammer", "Bullish Engulfing", "Morning Star", "Piercing Pattern", "Three White Soldiers"
    }
    bearish_patterns = {
        "Shooting Star", "Bearish Engulfing", "Evening Star", "Dark Cloud Cover", "Three Black Crows"
    }
    neutral_patterns = {
        "Doji", "Spinning Top", "Inside Bar"
    }

    for i in range(2, len(df)):
        signal = None

        o, h, l, c = df.iloc[i][['Open', 'High', 'Low', 'Close']]
        o1, h1, l1, c1 = df.iloc[i-1][['Open', 'High', 'Low', 'Close']]
        o2, h2, l2, c2 = df.iloc[i-2][['Open', 'High', 'Low', 'Close']]

        body = abs(c - o)
        upper_shadow = h - max(c, o)
        lower_shadow = min(c, o) - l

        if lower_shadow > body * 2 and upper_shadow < body * 0.5:
            signal = "Hammer"

        elif c > o and o1 > c1 and c > o1 and o < c1:
            signal = "Bullish Engulfing"

        elif c2 < o2 and abs(c1 - o1) < (h1 - l1) * 0.1 and c > o:
            signal = "Morning Star"

        elif o < c1 and c > (o1 + c1) / 2 and c < o1:
            signal = "Piercing Pattern"

        elif all(df.iloc[j]['Close'].item() > df.iloc[j]['Open'].item() for j in range(i-2, i+1)):
            signal = "Three White Soldiers"

        elif upper_shadow > body * 2 and lower_shadow < body * 0.5:
            signal = "Shooting Star"

        elif o > c and c1 > o1 and o < c1 and c > o1:
            signal = "Bearish Engulfing"

        elif c2 > o2 and abs(c1 - o1) < (h1 - l1) * 0.1 and c < o:
            signal = "Evening Star"

        elif o > c1 and c < (o1 + c1) / 2 and c > o1:
            signal = "Dark Cloud Cover"

        elif all(df.iloc[j]['Close'].item() < df.iloc[j]['Open'].item() for j in range(i-2, i+1)):
            signal = "Three Black Crows"

        elif abs(c - o) <= (h - l) * 0.1:
            signal = "Doji"

        elif body < (h - l) * 0.3 and upper_shadow > body and lower_shadow > body:
            signal = "Spinning Top"

        elif h < h1 and l > l1:
            signal = "Inside Bar"

        signals[i] = signal  # zapisz do właściwego indexu
        
        # Określ kategorię wzorca
        if signal in bullish_patterns:
            categories[i] = "Bullish"
        elif signal in bearish_patterns:
            categories[i] = "Bearish"
        elif signal in neutral_patterns:
            categories[i] = "Neutral"
        else:
            categories[i] = None

    df['Pattern'] = signals
    df['Pattern_Category'] = categories
    
    # Zwróć ostatni wykryty pattern (najnowszy)
    latest_pattern = signals[-1] if signals else None
    latest_category = categories[-1] if categories else None
    return df, latest_pattern, latest_category


