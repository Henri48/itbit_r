from itbit_api import itBitApiConnection
import json

with open('data.json') as json_file:
    data = json.load(json_file)


client_key = data['client_key']
secret_key = data['secret_key']
userId = data['userId']

#create the api connection
itbit_api_conn = itBitApiConnection(clientKey=client_key, secret=secret_key, userId=userId)

symbol = data['symbol']
order_book = itbit_api_conn.get_order_book(symbol).json()
print(json.dumps(order_book, indent = 2))

print("creating a new order...")
walletID = data['walletID']
side = data['side']
currency = data['currency']
amount = data['amount']
price = data['price']
instrument = data['instrument']
new_order = itbit_api_conn.create_order(walletID, side, currency, amount, price, instrument)

print(json.dumps(new_order, indent = 2))
