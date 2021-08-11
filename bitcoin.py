import cryptocompare
while True:
    print(cryptocompare.get_price("BTC", curr="USD"))