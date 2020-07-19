import requests
import time
import pandas as pd
from pandas.io.json import json_normalize
import json
import ccxt


def getTime():
    named_tuple = time.localtime()  # get struct_time
    Time = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    print(Time)


# config
symbol = "BTC-PERPETUAL"
timestampRecordUltil = 1592442000
maxExposure = 3000
MIN_TPRANGE = 20
timeFrame = "1h"
countBar = 50
apiKey = "K0dNactS"
secret = "NGsHWQPlozOrWNbaYUklFZA573iDnpL2haSzd4ODqr0"

# Set zone  an=a1+(n−1)d
high_edge = 15000
low_edge = 5000
quota = 100  # 1 นัด = 10$ = 1000$
usd_size = 10  # 10$
gap_zone = 100  # ~101.0101...

# exchange = ccxt.deribit({'apiKey': apiKey, 'secret': secret,
#                        'enableRateLimit': True, "urls": {"api": "https://test.deribit.com"}})

exchange = ccxt.deribit({
    'apiKey': apiKey, 'secret': secret,
    'enableRateLimit': True,
    'options': {
        'code': 'BTC',  # set default currency exchange-wide
        'fetchBalance': {'code': 'BTC'},  # set currency per method
        # default quote if no symbol is specified
        'fetchOpenOrders': {'code': 'BTC'},
        'fetchMyTrades': {'code': 'BTC'},
        # ...
    },
    'testnet': True,
    "urls": {"api": "https://test.deribit.com"}
})

# exchange.headers = {
#    'FTX-SUBACCOUNT': 'sub_1',
# }
exchange.load_markets()

# print(exchange.requiredCredentials)  # prints required credentials
# exchange.checkRequiredCredentials()  # raises AuthenticationError
# exchange.create_market_buy_order(symbol, 10)  # market_buy_order
print("\n=============exchange=============")
print(exchange)


print("\n=============fetch_balance=============")

balance = exchange.fetch_balance()
# print(exchange.has)
# data = json.load(balance)
df = pd.json_normalize(balance, 'total', ['BTC'],
                       record_prefix='total_')
print(df)


print("\n=============fetchMyTrades =============")
#my_trades = exchange.fetchClosedOrders(symbol)
my_trades = exchange.private_get_get_position({
    'instrument_name': 'BTC-PERPETUAL',
})

# print(my_trades)
my_trades = pd.json_normalize(my_trades)
df_curr_trade = pd.DataFrame(my_trades, columns=[
    'result.instrument_name', 'result.size', 'result.settlement_price', 'result.average_price'])

print(df_curr_trade)
total_amt = df_curr_trade['result.size'][0]
print('amount=', df_curr_trade['result.size'][0])

print("\n=============fetchOpenOrders=============")
open_trades = exchange.fetchOpenOrders()
df_open_trades = pd.DataFrame(open_trades, columns=[
    'id', 'datetime', 'symbol', 'price', 'amount'])

print(df_open_trades)
print('amount=', df_open_trades['amount'].sum())
total_amt = total_amt+df_open_trades['amount'].sum()
print("\n=============fetchTrades=============")
# if exchange.has['fetchTrades']:
# ensure you have called loadMarkets() or load_markets() method.
# for symbol in exchange.markets:
# time.sleep(exchange.rateLimit / 1000)  # time.sleep wants seconds
# print(symbol, exchange.fetch_trades(symbol))
resistance_price = 20000
support_price = 0

while True:
    Time = getTime()

    ####### Start calculation #############
    r1 = json.dumps(exchange.fetch_ticker('BTC-PERPETUAL'))
    market_price = json.loads(r1)
    n = (high_edge - market_price['last']) / gap_zone
    print("quota:" + str(quota))
    print("exp[amt]:" + str(total_amt))
    print("current quota used:" + str(int(total_amt/usd_size)))
    print("quota zone:" + str(int(n)))

    # calculate pivot point
    # (High + Low + Close) / 3 = PP (pivot point)
    # (2 x PP) – Low = First resistance level
    # (2 x PP) – High = First support level
    ohlcv = exchange.fetch_ohlcv(symbol, timeFrame, limit=2)
    df_ohlcv = pd.DataFrame(ohlcv)
    df_rename = df_ohlcv.rename(
        columns={0: 'Time', 1: 'Open', 2: 'High', 3: 'Low', 4: 'Close', 5: 'Volume'})

    pp = round((df_rename['High'][0] + df_rename['Low']
                [0] + df_rename['Close'][0]) / 3, 2)
    resistance_price = round(pp*2-df_rename['Low'][0], 2)
    support_price = round((pp * 2 - df_rename['High'][0]), 2)
    print("market_price: " + str(market_price['last']))
    print("pp: " + str(pp))
    print("Support: " + str(support_price))
    print("resistance: " + str(resistance_price))

    # check quota
    if int(n) > int(total_amt / usd_size):
        print("open buy limit")
        exchange.create_order(
            symbol, "limit", "buy", usd_size*(n-int(total_amt / usd_size)), support_price)

    elif int(n) < int(total_amt / usd_size):
        print("Close order.")

        for i in range(len(df_open_trades)):
            # cancel_orderby_id
            # print(df_open_trades['id'][i])
            exchange.cancel_order(df_open_trades['id'][i])

        curr_size_order = int(df_curr_trade['result.size'].sum() / usd_size)
        close_size = int(total_amt / usd_size) - int(n)
        print("diff "+str(int(close_size)))
        # print(size_order)
        exchange.create_market_sell_order(
            symbol, close_size*usd_size)  # market_sell_order
        # print("size_order")
        # print(size_order)

        if int(n) > int(total_amt / usd_size):
            print("open buy limit")
            exchange.create_order(
                symbol, "limit", "buy", usd_size*(n-int(total_amt / usd_size)), support_price)

        ####### End calculation #############
    print("================================")
    # Re-check position
    print("\n=============fetchMyTrades =============")
    #my_trades = exchange.fetchClosedOrders(symbol)
    my_trades = exchange.private_get_get_position({
        'instrument_name': 'BTC-PERPETUAL',
    })

    my_trades = pd.json_normalize(my_trades)
    df_curr_trade = pd.DataFrame(my_trades, columns=[
        'result.instrument_name', 'result.size', 'result.settlement_price', 'result.average_price'])
    print(df_curr_trade)
    total_amt = df_curr_trade['result.size'][0]

    print("\n=============fetchOpenOrders=============")
    open_trades = exchange.fetchOpenOrders()
    df_open_trades = pd.DataFrame(open_trades, columns=[
        'id', 'datetime', 'symbol', 'price', 'amount'])

    total_amt = total_amt+df_open_trades['amount'].sum()
    print(df_open_trades)

    time.sleep(10)  # 10 sec.
