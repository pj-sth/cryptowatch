import requests

BASE_URL = "https://api.coingecko.com/api/v3"

def fetch_trending(limit=5):
    """Fetch top gainers and losers in the last 24 hours"""
    try:
        url = f"{BASE_URL}/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 100,
            "page": 1,
            "price_change_percentage": "24h"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        sorted_data = sorted(data, key=lambda x: x["price_change_percentage_24h"] or 0, reverse=True)

        gainers = sorted_data[:limit]
        losers = sorted_data[-limit:]

        return gainers, losers
    except requests.RequestException as e:
        print(f"Error fetching trending data: {e}")
        return None, None

def display_trending():
    """Display formatted top gainers and losers"""
    gainers, losers = fetch_trending()

    if not gainers or not losers:
        print("Unable to fetch trending data.")
        return
    
    print("\nTop Gainers (24h):")
    for coin in gainers:
        print(f" {coin['name']} ({coin['symbol'].upper()}) - +{coin['price_change_percentage_24h']:.2f}%")

    print("\nTop Losers (24h):")
    for coin in reversed(losers):
        print(f" {coin['name']} ({coin['symbol'].upper()}) - {coin['price_change_percentage_24h']:.2f}%")

    print("\nMarket trend overview completed.\n")