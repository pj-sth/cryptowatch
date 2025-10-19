import argparse
from cryptowatch import api, storage

def main():
    parser = argparse.ArgumentParser(
        description = "CryptoWatch CLI - Track cryptocurrency prices & watchlist"
    )

    parser.add_argument("--price",help="Fetch current price of a cryptocurrency (e.g. bitcoin)")
    parser.add_argument("--add",help="Add a coin to your watchlist")
    parser.add_argument("--watchlist",action="store_true",help="View your saved watchlist")

    args = parser.parse_args()

    if args.add:
        storage.add_to_watchlist(args.add)
    elif args.watchlist:
        watchlist = storage.load_watchlist()
        if not watchlist:
            print("Your watchlist is empty. Use '--add' to add coins.")
            return
        print("\n Your Watchlist:\n")
        for coin in watchlist:
            coin_data = api.fetch_price(coin)
            if coin_data:
                print(f"{coin_data['name']} ({coin_data['symbol']}): ${coin_data['price_usd']}")
        print("\n End of watchlist.\n")

    if args.price:
        coin_data = api.fetch_price(args.price)
        if coin_data:
            print(f"\n{coin_data['name']} ({coin_data['symbol']})")
            print(f"Price (USD): ${coin_data['price_usd']}")
            print(f"Market Rank: #{coin_data['rank']}")
            print(f"24h Change: {coin_data['change_24h']:.2f}%\n")
        else:
            parser.print_help()

if __name__ == "__main__":
    main()