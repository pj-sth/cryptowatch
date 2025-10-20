import json
import os


WATCHLIST_FILE = "watchlist.json"

def load_watchlist():
    """Load the user's save watchlist"""
    if not os.path.exists(WATCHLIST_FILE):
        return []
    try:
        with open(WATCHLIST_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
    
def save_watchlist(watchlist):
    """Save updated watchlist"""
    with open(WATCHLIST_FILE, "w") as file:
        json.dump(watchlist, file, indent=2)

def add_to_watchlist(coin_id):
    """Add a new coin to the watchlist"""
    watchlist = load_watchlist()
    if coin_id.lower() not in [c.lower() for c in watchlist]:
        watchlist.append(coin_id.lower())
        save_watchlist(watchlist)
        print(f"Added '{coin_id}' to your watchlist.")
    else:
        print(f"'{coin_id}' is already in your watchlist.")