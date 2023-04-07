#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3

db= sqlite3.connect ('stockprice.sqlite3')

c= db.cursor()

c.execute('DROP TABLE IF EXISTS stockprice;')

c.execute('CREATE TABLE stockprice (symbol TEXT PRIMARY KEY, price INTEGER, percentage_change FLOAT, marketcap INTEGER, sector TEXT, volume INTEGER);')


sqlinsert = 'INSERT INTO stockprice (symbol, price, percentage_change, marketcap, sector, volume) VALUES (?,?,?,?,?,?);' 

values = [
('SYMBOL', 'PRICE', 'PERCENTAGE_CHANGE', 'MARKETCAP', 'SECTOR', 'VOLUME'),
('AAPL',157.69 ,0.50,2733944215674.00,'Technology',40908280),
('AMZN',122.32 ,0.11,1244858336089.00,'Consumer_Discretionary',20574910),
('COST',502.91 ,0.68,222770895348.00,'Consumer_Discretionary',665650),
('GOOG',102.40 ,0.56,1335705600000.00,'Technology',9615496),
('GOOGL',101.77 ,0.62,1327487880000.00,'Technology',9546753),
('META',146.39 ,0.21,393430220816.00,'Technology',18705897),
('MSFT',245.77 ,1.37,1832931305906.00,'Technology',9446906),
('NVDA',136.14 ,3.32,338988600000.00,'Technology',36008474),
('PEP',171.88 ,1.75,237208982987.00,'Consumer_Staples',1983288),
('TSLA',309.22 ,0.16,968921266864.00,'Consumer_Discretionary',27650025)
]

c.executemany(sqlinsert, values)

db.commit()

#Create an input so the user can choose which stock to show
symbol = input('Input the stock symbol you want information about! { AAPL, AMZN, COST, GOOG, GOOGL, META, MSFT, NVDA, PEP, TSLA, or ALL} --> ')
symbol = symbol.upper()


#Return the row that is correlated with the input of the user if a valid symbol is added
c.execute('SELECT * FROM stockprice WHERE symbol = ?;', [symbol])
row = c.fetchone()
if row:
    print()
    print("Symbol", "Price", "Percent_Change", "MarketCap", "Industry", "Volume")
    print(row)
# Return all of the rows in the Database
elif symbol == "ALL":
    c.execute('SELECT * FROM stockprice;')
    rows = c.fetchall()
    print()
    for i in rows:
        print(i)
else:
    print()
    print('no data was returned')

    
db.close ()


# In[ ]:




