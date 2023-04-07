#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests_html
from tabulate import tabulate
from prettytable import PrettyTable


session = requests_html.HTMLSession()

# Input which symbols you want to look up
symbol = input ('Please input the symbol you want to look up. You can look up seperate symbols by seperating them with a comma.  ')
symbol = symbol.upper()
symbol_list = symbol.split(", ")
print(symbol_list)

history1 = input('how many past days do you want to see? ')
history = int(history1)
print("\n")




#Create headers for table
t = PrettyTable(['Historic Date', 'Openprice', 'Closeprice', 'Difference', 'Result'])

#Loop through every symbol and scrape it from marketwatch.com
for i in symbol_list:
    for x in range(1, history+1):
        
        url = session.get('https://finance.yahoo.com/quote/' + i+'/history/')
            
        #scraping the finance.yahoo.com website
            
        stockname = url.html.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1', first=True)
        date = url.html.xpath ('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+str(x)+']/td[1]/span', first=True)
        openprice = url.html.xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+str(x)+']/td[2]/span', first=True)
        closeprice = url.html.xpath('//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr['+str(x)+']/td[5]/span', first=True)
        stockprice= url.html.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]', first=True)
            

            #Only scraping the first value that I want, also doing try/except so that the program won't crash if a value is not found
        stockname = stockname.text.split("\n")[0]
        try:
            stockprice = stockprice.text.split("\n")[0]
        except:
            stockprice = 'Invalid'
        try:
             date = date.text.split("\n")[0]
        except:
            date = "Invalid"
        try:
            openprice = openprice.text.split("\n")[0]
        except:
            openprice = "Invalid"
        try:
            closeprice = closeprice.text.split("\n")[0]
        except:
            closeprice = "Invalid"
            
        if ','  in closeprice or ',' in openprice:
            closeprice= closeprice.replace(',', '')
            openprice= openprice.replace(',', '')
            
        closeopendiff= round(float(closeprice)-float(openprice),2)
        closeopendiff= float(closeopendiff)

        if closeopendiff < 0:
            result = "\033[1;31m LOSS \033[0m"
        else:
            result = "\033[1;32m GAIN \033[0m"

        #Creating the variable 'value' to store the data from each symbol    
        value = date, '$'+ openprice, '$'+ closeprice , closeopendiff, result
        t.add_row(value)

        #Showing an error if an invalid stock symbol is put in
        #except:
            #print ('Please seperate symbols with a comma and space or enter a valid stock symbol for:', i)
            #print('\n')
    print("The following table is for:", "\033[1m\033[4m"+ stockname+",\033[0m"," which has a current stockprice of:", "\033[1m\033[4m$"+ stockprice+".\033[0m")
    print(t)
    print('\n')
    t.clear_rows()

