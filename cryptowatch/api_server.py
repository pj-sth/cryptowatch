from fastapi import FastAPI
from cryptowatch import api, storage, trending

app = FastAPI(title="CryptoWatch API", version="1.0")

@app.get("/")
def root():
    return {"message": "Welcome to CryptoWatch API"}

@app.get("/price/{coin}")
def get_price(coin: str):
    coin_data = api.fetch_price(coin)
    if not coin_data:
        return {"error": "Coin not found"}
    return coin_data

@app.get("/watchlist")
def get_watchlist():
    watchlist = storage.load_watchlist()
    if not watchlist:
        return {"message": "Your watchlist is empty."}
    coins = []
    for c in watchlist:
        data = api.fetch_price(c)
        if data:
            coins.append(data)
    return {"watchlist": coins}

@app.get("/trending")
def get_trending():
    gainers, losers = trending.fetch_trending()
    if not gainers or not losers:
        return {"error": "Unable to fetch trending data."}
    return {"gainers": gainers, "losers": losers}