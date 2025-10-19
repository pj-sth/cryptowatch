import json
import os
from cryptowatch import api

PORTFOLIO_FILE = "portfolio.json"

def load_portfolio():
    """Load portfolio data"""
    if not os.path.exists(PORTFOLIO_FILE):
        return {}
    try:
        with open(PORTFOLIO_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}
    
def save_portfolio(portfolio):
    """Save updated portfolio"""
    with open(PORTFOLIO_FILE, "w") as file:
        json.dump(portfolio, file, indent=2)

def add_coin(coin_id, amount):
    """Add coin and amount to portfolio"""
    portfolio = load_portfolio()
    coin_id = coin_id.lower()

    if coin_id in portfolio:
        portfolio[coin_id] += amount
    else:
        portfolio[coin_id] = amount

    save_portfolio(portfolio)
    print(f"Added {amount} {coin_id.upper()} to your portfolio.")

def show_portfolio():
    """Display all coins and total portfoilo value"""
    portfolio = load_portfolio()
    if not portfolio:
        print("Your portfolio is empty. Use '--buy' to add options.")
        return
    
    print("\nYour Portfolio:\n")
    total_value = 0

    for coin, amount in portfolio.items():
        coin_data = api.fetch_price(coin)
        if not coin_data:
            continue
        value = amount * coin_data["price_usd"]
        total_value += value
        print(f"{coin_data['name']} ({coin_data['symbol']}) : {amount} -> ${value:,.2f}")
    
    print(f"\nTotal Portfolio Value: ${total_value:,.2f}\n")