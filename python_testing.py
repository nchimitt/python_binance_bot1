from binance.client import Client
api_key = #use your own
api_secret = #use your own
client = Client(api_key, api_secret)
tickers = client.get_symbol_ticker()
#tickers: list of dictionaries of type {symbol:__,price:__}
print (tickers[0]['symbol'])
print (tickers[0]['price'])
