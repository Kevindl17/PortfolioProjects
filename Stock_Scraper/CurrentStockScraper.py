#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests_html
from tabulate import tabulate
from prettytable import PrettyTable

session = requests_html.HTMLSession()

# Input which symbols you want to look up
symbol = input ('Please input the symbol you want to look up. You can look up seperate symbols by seperating them with a comma.  ')
symbol = symbol.upper()
symbol_list = symbol.split(", ")
print(symbol_list)
print("\n")

#Create headers for table
t = PrettyTable(['Symbol', 'Stockname', 'Stockprice', 'Marketcap', 'PE Ratio'])

#Loop through every symbol and scrape it from marketwatch.com
for i in symbol_list:
    try:
    
        url = session.get('https://www.marketwatch.com/investing/stock/' + i)
        

        #scraping the Marketwatch.com website
        stockname = url.html.xpath('//*[@id="maincontent"]/div[2]/div[2]/div/div[2]/h1', first=True)
        stockprice = url.html.xpath('//*[@id="maincontent"]/div[2]/div[3]/div/div[2]/h2/bg-quote', first=True)
        marketcap = url.html.xpath('//*[@id="maincontent"]/div[6]/div[1]/div[1]/div/ul/li[4]/span[1]', first=True)
        peratio= url.html.xpath('//*[@id="maincontent"]/div[6]/div[1]/div[1]/div/ul/li[9]/span[1]', first=True)

        #Only scraping the first value that I want, also doing try/except so that the program won't crash if a value is not found
        stockname = stockname.text.split("\n")[0]
        try:
            stockprice = stockprice.text.split("\n")[0]
        except:
            stockprice = 'Invalid'
        try:
            marketcap = marketcap.text.split("\n")[0]
        except:
            marketcap = "Invalid"
        try:
            peratio = peratio.text.split("\n")[0]
        except:
            peratio = "Invalid"

        #Creating the variable 'value' to store the data from each symbol    
        value = i, stockname, stockprice, marketcap, peratio
        t.add_row(value)


    #Showing an error if an invalid stock symbol is put in
    except:
        print ('Please seperate symbols with a comma and space or enter a valid stock symbol for:', i)
        print('\n')

print(t)


# In[ ]:




