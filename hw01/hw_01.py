import ccxt
import json


def FTX():
    print("\nHere's FTX!\n")
    ftx_api_key = input("\nAPI Key: ")
    ftx_secret_key = input("\nSecret Key: ")
    exchange = ccxt.exchange = ccxt.ftx({
        'apiKey' : ftx_api_key,
        'secret' : ftx_secret_key,
        'enableRateLimit' : True } )

    #exchange = ccxt.exchange = ccxt.ftx({
    #    'apiKey' : "xx",
    #    'secret' : "xxx",
    #    'enableRateLimit': True})
		
    r1 = json.dumps(exchange.fetch_ticker('BTC-PERP'))
    r2 = json.dumps(exchange.fetch_ticker('XRP-PERP'))
    dataPriceBTC = json.loads(r1)
    dataPriceXRP = json.loads(r2)
    print("\n",exchange)
    print('BTC-PERP =',dataPriceBTC['last'])
    print('XRP-PERP =', dataPriceXRP['last'])
    #print("PORT BALANCE =",exchange.fetch_balance())
    ftx_choice = ''
    while ftx_choice != 'q':
        # Give all the choices in a series of print statements.
        print("\nSelect Exhange.")
        print("[1] Enter 1 : Account Info.")
        print("[2] Enter 2 : Trade.")
        print("[3] Enter 3 : Order Info.")
        print("[q] Enter q : Back to main menu.") 

        # Ask for the user's choice.
        ftx_choice = input("\nWhat would you like to do? ")

        # Respond to the user's choice.
        if ftx_choice == '1':
            acct_info(exchange)
        elif ftx_choice == '2':
            trading(exchange)
        elif ftx_choice == '3':
            order_info(exchange)
        elif ftx_choice == 'q':
            print("\nThanks for playing. See you later.\n")
        else:
            print("\nI don't understand that choice, please try again.\n")


def Karken():
    print("\nHere's Karken!\n")
    api_key = input("\nAPI Key: ")
    secret_key = input("\nSecret Key: ")
    exchange = ccxt.exchange = ccxt.kraken({
        'apiKey' : api_key,
        'secret' : secret_key,
        'enableRateLimit' : True } )

    #exchange = ccxt.exchange = ccxt.kraken({
    #    'apiKey' : "xxx",
    #    'secret' : "xxxx",
    #    'enableRateLimit': True})
		
    r1 = json.dumps(exchange.fetch_ticker('BTC/USD'))
    r2 = json.dumps(exchange.fetch_ticker('XRP/USD'))
    dataPriceBTC = json.loads(r1)
    dataPriceXRP = json.loads(r2)
    print("\n",exchange)
    print('BTC/USD =',dataPriceBTC['last'])
    print('XRP/USD =', dataPriceXRP['last'])
    #print("PORT BALANCE =",exchange.fetch_balance())
    kk_choice = ''
    while kk_choice != 'q':
        # Give all the choices in a series of print statements.
        print("\nSelect Exhange.")
        print("[1] Enter 1 : Account Info.")
        print("[2] Enter 2 : Trade.")
        print("[3] Enter 3 : Order Info.")
        print("[q] Enter q : Back to main menu.") 

        # Ask for the user's choice.
        kk_choice = input("\nWhat would you like to do? ")

        # Respond to the user's choice.
        if kk_choice == '1':
            acct_info(exchange)
        elif kk_choice == '2':
            trading(exchange)
        elif kk_choice == '3':
            order_info(exchange)
        elif kk_choice == 'q':
            print("\nThanks for playing. See you later.\n")
        else:
            print("\nI don't understand that choice, please try again.\n")


def trading(exchange):
    print("==========================")
    print("==========================")
    print(exchange)
    print("\nHere's trading!\n")
    trade_flag = ''
	#ตรวจเช็ค PRODUCT ที่สามารถเทรดได้
    print("PRODUCT =", exchange.symbols)

    try:
        while trade_flag != 'q':
            # Give all the choices in a series of print statements.
            print("\nSelect Exhange.")
            print("[1] Enter 1 : BUY.")
            print("[2] Enter 2 : BUY LIMIT.")
            print("[3] Enter 3 : SELL.")
            print("[4] Enter 4 : SELL LIMIT.")
            print("[5] Enter 5 : Check Order.")
            print("[6] Enter 6 : Cancel Order.")
            print("[q] Enter q : Go to main menu.") 
            # Ask for the user's choice.
            trade_flag = input("\nWhat would you like to do? ")

    		#order properties
            reduceOnly = False
            postOnly =  False
            ioc = False

            # Respond to the user's choice.
            if trade_flag == '1':
                print("[1] BUY.")
                product = input("\nProduct\nEx. 'BTC/USD', BTC-PERP : ")
                size_order = input("\nSize of order: ")
                exchange.create_market_buy_order(product, size_order)  # market_buy_order
			   
            elif trade_flag == '2':
                print("[2] BUY LIMIT.")
                product = input("\nProduct\nEx. 'BTC/USD', BTC-PERP : ")
                price = input("\nprice: ")
                size_order = input("\nSize of order: ")
                exchange.create_order(product, "limit", "buy", size_order, price)
				
            elif trade_flag == '3':
                print("[3] SELL.")
                product = input("\nProduct\nEx. 'BTC/USD', BTC-PERP : ")
                size_order = input("\Size of order: ")
                exchange.create_market_sell_order(product, size_order)  # market_sell_order
				
            elif trade_flag == '4':
                print("[4] SELL LIMIT.")
                product = input("\nProduct\nEx. 'BTC/USD', BTC-PERP : ")
                price = input("\nprice: ")
                size_order = input("\nSize of order: ")
                exchange.create_order(product, "limit", "sell", size_order, price)
            elif trade_flag == '5':
                print("[5] Check Order.")
                print(exchange.fetchOpenOrders())
            elif trade_flag == '6':
                print("[6] Cancel Order.")
                order_id = input("\nCancel id: ")
                exchange.cancel_order(order_id) # cancel_orderby_id
            elif trade_flag == 'q':
                print("\Go to main menu.\n")

            else:
                print("\nI don't understand that choice, please try again.\n")
    except Exception as inst:
        print(inst)          # __str__ allows args to be printed directly,

def acct_info(exchange):
    print("==========================")
    print("==========================")
    print(exchange)
    print("\nHere's acct_info!\n")
	#ตรวจเช็ค BALANCE ของ PORTFOLIO
    print("PORT BALANCE =",exchange.fetch_balance())

def order_info(exchange):
    print("==========================")
    print("==========================")
    print(exchange)
    print("\nHere's order_info!\n")
    print(exchange.fetchOpenOrders())


# Give the user some context.
print("\nWelcome to the nature center. What would you like to do?")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("\nSelect Exhange.")
    print("[1] Enter 1 : FTX.")
    print("[2] Enter 2 : Kraken.")
    print("[q] Enter q to quit.")

    # Ask for the user's choice.
    choice = input("\nWhat would you like to do? ")

    # Respond to the user's choice.
    if choice == '1':
        FTX()
    elif choice == '2':
        Karken()
    elif choice == 'q':
        print("\nThanks for playing. See you later.\n")
    else:
        print("\nI don't understand that choice, please try again.\n")


# Print a message that we are all finished.
print("Thanks again, bye now.")
