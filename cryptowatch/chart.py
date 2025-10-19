import requests
import matplotlib.pyplot as plt
from datetime import datetime

BASE_URL = "https://api.coingecko.com/api/v3"

def fetch_historical_data(coin_id, days=7):
    """Fetch historical market data for a coin from CoinGecko"""
    try:
        url = f"{BASE_URL}/coins/{coin_id}/market_chart"
        params = {"vs_currency": "usd", "days": days}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        prices = data.get("prices", [])
        if not prices:
            print("No price data found.")
            return None
        
        timestamps = [datetime.fromtimestamp(p[0] / 1000) for p in prices]
        values = [p[1] for p in prices]
        return timestamps, values
    except requests.RequestException as e:
        print(f"Error fetching historical data: {e}")
        return None
    
def plot_chart(coin_id, days=7):
    """Plot the coin's price trend"""
    result = fetch_historical_data(coin_id, days)
    if not result:
        return
    
    timestamps, values = result

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, values, label=f"{coin_id.capitalize()} ({days}-day trend)", linewidth=2)
    plt.title(f"{coin_id.capitalize()} Price Trend (Last {days} Days)")
    plt.xlabel("Date")
    plt.ylabel("Price {USD}")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()