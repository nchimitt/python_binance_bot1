from binance.client import Client
api_key = #Enter your own API Key
api_secret = #Enter your own API Secret Key
client = Client(api_key, api_secret)
hi = [];
hi = client.get_klines(symbol='ETHBTC',interval='5m',limit=100)
