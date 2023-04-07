#!/usr/bin/env python
# coding: utf-8

# In[195]:


import datetime
#The program starts by asking the user what he or she wants the calculator to do.
start= input("Choose 1 or 2: (option 1 = how far your birthday is from christmas // option 2 = how many days there are between two dates ")
#If option 1 is chosen, the program shows how many days away your birthday is from christmas & shows the current UTC time

if start in ["option 1", "'option 1'", "1"]:

    #Asks the user to input their date of birth and strips the time    
    try:
        birthday = input("what is your date of birth? (YYYY/MM/DD)")
        bd = datetime.datetime.strptime(birthday, "%Y/%m/%d")
    #If the entered date is not valid, an error message displays
    except: 
        print("please enter your birthdate in the YYYY/MM/DD format")
        
    #Variable 'd' gets the current day/time/year value, variable 'tz' is used to display the timezone value later, variable 'utc' is used to show the time that it is in UTC right now
    #Variable 'christmas' is used to assign the closest christmas date to this variable
    d = datetime.datetime.now()
    tz = datetime.timezone(datetime.timedelta())
    utc= datetime.datetime.now(tz)
    christmas = datetime.datetime(d.year, 12, 25)

    #Gives the current year to the birthday
    bdy = datetime.datetime(d.year, bd.month, bd.day)

    #Makes sure that christmas is always bigger than the birthday date
    if christmas < bdy:
        christmas = datetime.datetime(d.year, 12, 25)
        bdy = datetime.datetime (d.year-1, bd.month, bd.day)

    print("You were born in", bd.year, "and your birthday is", (christmas-bdy).days, "days away from christmas." )
    print("The current time for the UTC timezone is:", tz, utc.hour, ":", utc.minute)
    
#If option 2 is chosen, the program shows how many days there are between two dates
elif start in ["option 2", "'option 2'", "2"]:
    
    #Asks the user to input the two dates that are being used for calculation
    try:
        begin_date = input("What is the begin date (YYYY/MM/DD)")
        end_date = input("What is the end date (YYYY/MM/DD)")
        # Strips the two dates and makes sure that it will only be displayed in date value without time
        begin_date_stripped = datetime.datetime.strptime(begin_date, "%Y/%m/%d").date()
        end_date_stripped = datetime.datetime.strptime(end_date, "%Y/%m/%d").date()
        date_calculation = (end_date_stripped - begin_date_stripped).days
        first_date = begin_date_stripped
        second_date = end_date_stripped
        
        if end_date_stripped <= begin_date_stripped:
            date_calculation = (begin_date_stripped - end_date_stripped ).days
            first_date = end_date_stripped
            second_date = begin_date_stripped
            
        
    except: 
        print("please enter the date in the YYYY/MM/DD format")
         
    print("There are", date_calculation, "days between", first_date, "&", second_date)

#If a wrong option is entered, this will be displayed
else: 
    print("ERROR: Please enter '1' or '2'")


# In[ ]:




