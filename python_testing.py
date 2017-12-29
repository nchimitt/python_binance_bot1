from binance.client import Client
api_key = #enter your key
api_secret = #still enter your key
client = Client(api_key, api_secret)
prices = client.get_all_tickers()
