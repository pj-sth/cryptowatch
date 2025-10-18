import requests

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/coins/{}"

def fetch_price(coin_id: str):
    """Fetch real-time crypto data from CoinGecko"""
    url = COINGECKO_API_URL.format(coin_id.lower())
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        market_data = data.get("market_data", {})
        current_price = market_data.get("current_price", {}).get("usd")
        market_cap_rank = data.get("market_cap_rank")
        change_24h = market_data.get("price_change_percentage_24h")

        if current_price is None:
            raise ValueError("Price data unavailable")

        return {
            "name": data.get("name"),
            "symbol": data.get("symbol").upper(),
            "price_usd": current_price,
            "rank": market_cap_rank,
            "change_24h": change_24h
        }

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Network error: {e}")
    except ValueError as e:
        print(f"[ERROR] {e}")
    except KeyError:
        print("[ERROR] Unexpected API response format")
    return None
