import argparse
from cryptowatch import api

def main():
    parser = argparse.ArgumentParser(
        description = "CryptoWatch CLI - Track cryptocurrency prices"
    )

    parser.add_argument(
        "--price",
        help="Fetch current price of a cryptocurrency (e.g. bitcoin)"
    )

    args = parser.parse_args()

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