import argparse
from cryptowatch import api, storage, portfolio

def main():
    parser = argparse.ArgumentParser(
        description = "CryptoWatch CLI - Track cryptocurrency prices, watchlist & portfolio"
    )

    parser.add_argument("--price",help="Fetch current price of a cryptocurrency (e.g. bitcoin)")
    parser.add_argument("--add",help="Add a coin to your watchlist")
    parser.add_argument("--watchlist",action="store_true",help="View your saved watchlist")
    parser.add_argument("--buy", nargs=2, metavar=('COIN', 'AMOUNT'), help="Add coin and amount to portfolio")
    parser.add_argument("--portfolio", action="store_true", help="View your portfolio")

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

    elif args.buy:
        coin, amount = args.buy
        try:
            portfolio.add_coin(coin, float(amount))
        except ValueError:
            print("Invalid amount. Use a number, e.g. '--buy bitcoin 0.5'")

    elif args.portfolio:
        portfolio.show_portfolio()

    elif args.price:
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