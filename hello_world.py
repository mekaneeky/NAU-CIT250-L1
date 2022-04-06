import requests 

try:
    btc_price = requests.get("https://blockchain.info/ticker")
    btc_price = btc_price.json()["USD"]["last"]
    print("Hello World")
    print(f"Bitcoin is now at ${int(btc_price)}")
except:
    print("Hello World ! Can't fetch bitcoin price")

    
    

