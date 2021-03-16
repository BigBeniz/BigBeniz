### BigBeniz entertaiment presents a Primitive Trader Bot for Binance Ver.1.2
###Fixed API Communication error
from binance.client import Client ##pip3 install python-binance
from binance.enums import *
import time
import os
from time import sleep

api_key = ("")#Binance API Key
api_secret = ("")#Binance API secret key
client = Client(api_key, api_secret) #login to binance

while True:

    def ballance_checker1():
        try:
            balance_usdt = client.get_asset_balance(asset=(asset1))# balance of usdt(fiat)
            balance_usdt1 = (balance_usdt["free"])
        except:
            balance_usdt1 = 0
        try:   
            balance_coin = client.get_asset_balance(asset=(asset2))# balance of coin
            balance_coin1 = (balance_coin["free"])
        except:
            balance_coin1 = 0
        
        
        
        balance_coin1 = (balance_coin["free"])
        print((balance_usdt["free"]) + (" ") + (asset1) + (" Free")) # free usdt(fiat) balance
        print((balance_usdt["locked"]) + (" ") + (asset1) + (" Locked")) # locked usdt(fiat) balance
        print((balance_coin["free"]) + (" ") + (asset2) + (" Free")) # free coin balance
        print((balance_coin["locked"]) + (" ") + (asset2) + (" Locked")) # locked coin balance
        pricea = 100 * float(price)
        if float(balance_usdt1) >= pricea:
            finished12 = (format(float(price), '.5f'))
            print(finished12)
            try:
                price1b = (float(price)) / 100
                price2b = 100 - (int(procent))
                price3b = price1b * price2b
                finished1b = (format(float(price3b), '.5f'))
                order = client.order_limit_buy(symbol=(symbol1), quantity=(order_volume), price=(float(finished1b)))
                print("Buy was made")
            except:
                print("Wild API Error apear on Buy ")
                ballance_checker1()
            

        elif float(balance_coin1) >= order_volume:
            price1 = (float(price)) / 100
            price2 = 100 + (int(procent))
            price3 = price1 * price2
            finished1 = (format(float(price3), '.5f'))
            try:
                order = client.order_limit_sell(symbol=(symbol1), quantity=(order_volume), price=(float(finished1)))
            except:
                print("Wild API Error apear ")
                ballance_checker1()               
            print("Sell was made")
        else:
            temp_file()
        
    def temp_file():
        os.system("rm /home/dan/Desktop/Binance/*")
        order_checker()
        
    def order_checker():
        try:
            orders = client.get_open_orders(symbol=(symbol1))
        except:
            time.sleep(5)
            order_checker()
        number_of_order = len(orders)
        
        for i in range(number_of_order):
           order1 = orders[i]
           orderid = (order1["orderId"])
           
           PATH2 = ('/home/dan/Desktop/Binance/' + str(orderid))
           if os.path.isfile(PATH2) and os.access(PATH2, os.R_OK):
               if i == number_of_order - 1:
                   timeout_checker()
               else:
                   continue
           else:
               os.system('touch /home/dan/Desktop/Binance/' + str(orderid))
           
           
           
    def timeout_checker():
        arr = os.listdir('/home/dan/Desktop/Binance/')
        if len(arr) == 100:##################SETTING Maximum order operate
            print(("Max number of order was rached waiting ") + str((sleeper1) / 60) + ("min..."))
            time.sleep(sleeper1) 
            timeout_checker()  
        else:
            temp_file()
            print(("Waiting ") + str((sleeper) / 60) + ("min...") + (" for next order update.."))
            time.sleep(sleeper)
            ballance_checker1()
    

    symbol1 = ("XRPUSDT")##################SETTING TRADING PAIR
    asset1 = ("USDT")##################SETTING TRADING asset (fiat)
    asset2 = ("XRP")##################SETTING TRADING asset (crypto)
    order_volume = 30 ##################SETTING TRADING Volume of asset
    sleeper = 30 ##################SETTING time in second for refresh if not maximum order meet
    sleeper1 = 300 ##################SETTING time in second for refresh if maxmimum order meet
    procent = 2.5 ##################SETTING Set procent of predicted earnings
    
    
    try:
        info = client.get_avg_price(symbol=(symbol1)) # get price for trading pair
    except:
        print("Wild API Error apear ")
    price = (info["price"]) # price filter
    try:
        orders = client.get_open_orders(symbol=(symbol1))
    except:
        print("Wild API Error apear ")   

    if len(orders) == 0: # in case no order, initiate start order depend on ballance 
        ballance_checker1()
    else: # if order is found going to check how many order are avilable
        order_checker()
