from itbit_api import itBitApiConnection
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-client_key','--ck', help="insert the client Key")
parser.add_argument('-secret_key','--sk', help="insert the secret key")
parser.add_argument('-userId','--uI', help="insert the userId")
args = parser.parse_args()


if (args.ck is None):
    client_key = input("Client_Key is necessary.\nclient_Key:")
else:
    client_key = args.ck

if (args.sk is None):
    secret_key = input("Secret_Key is necessary.\nsecret_Key:")
else:
    secret_key = args.sk

if (args.uI is None):
    userId = input("User_ID is necessary.\nuser_ID:")
else:
    userId = args.uI

#print("\n\nclient_Key: "+client_key+" \nsecret_Key: "+secret_key+" \nUser_ID: "+userId)
#create the api connection
itbit_api_conn = itBitApiConnection(clientKey=client_key, secret=secret_key, userId=userId)

symbol = input("Symbol:")
order_book = itbit_api_conn.get_order_book(symbol).json()
print(json.dumps(order_book, indent = 2))

print("creating a new order")
walletID = input("WalletID:")
side = input("Side:")
currency = input("Currency:")
amount = input("Amount:")
price = input("Price:")
instrument = input("Instrument:")
new_order = itBitApiConnection(walletID, side, currency, amount, price, instrument)

print(json.dumps(new_order, indent = 2))
