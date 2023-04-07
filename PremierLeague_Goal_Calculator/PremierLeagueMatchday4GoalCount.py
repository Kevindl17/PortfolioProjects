#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[207]:


#Premier League (English soccer competition) results from matchday 4
# Original data from premierleague.com
# data in format of ['Date', 'Home Team', 'Away Team', 'End result', 'Minute of 1st goal', 'Minute of 2nd goal', 'Minute of 3rd goal', 'Minute of 4th goal', 'Minute of 5th goal', 'Minute of 6th goal', 'Minute of 7th goal', 'Minute of 8th goal', 'Minute of 9th goal', 'Minute of 10th goal']

PremierLeagueMD4 = [
['8/27/2022', "Southampton", "Manchester United", "0-1", "55", "NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL","NULL"],
['8/27/2022', "Chelsea", "Leicester City", "2-1", "47", "63", "66", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"],
['8/27/2022', "Brighton", "Leeds United", "1-0", "66", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"],
['8/27/2022', "Manchester City", "Crystal Palace", "4-2", "4", "21", "53", "62", "70", "81", "NULL", "NULL", "NULL", "NULL"],
['8/27/2022', "Liverpool", "Bournemouth", "9-0", "3", "6", "28", "31", "45", "46", "62", "80", "85", "NULL"],
['8/27/2022', "Brentford", "Everton", "1-1", "24", "84", "NULL", "NULLNULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"],
['8/27/2022', "Arsenal", "Fulham", "2-1", "56", "64", "86", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"],
['8/28/2022', "Wolverhampton", "Newcastle United", "1-1", "38", "90", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"],
['8/28/2022', "Aston Villa", "West Ham", "0-1", "74", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"],
['8/28/2022', "Forest", "Tottenham Hotspurs", "0-2", "5", "81", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
]

import csv
with open("PremierLeagueMD4.csv", "w", newline='') as f:
    fw = csv.writer(f)
    for x in PremierLeagueMD4:
        fw.writerow(x)
print("**DATA LOADED CORRECTLY**")

import csv
# \033[4m is used to UNDERLINE text & \033[1m is used to BOLD text. \033[0m is used to make sure the text that follows will be normal 
print("\033[4m\033[1mThis calculator can show you how many goals were scored in the Premier League on Matchday 4 between or after a certain minute\033[0m")

# The program starts by asking the user what he or she wants the calculator to do.
start= input("Choose one of two options: (option 1 = pick two time intervals and see how many goals are scored between these two // option 2 = pick one time interval and see how many goals were scored after this time) ")

# If option 1 is chosen, the program takes two time intervals and counts how many goals were scored between these two minutes
if start in ["option 1", "'option 1'", "1"]:
    try:
        begin_minute = int(input("Enter minute to see how many goals were scored after this minute: "))
        end_minute = int(input("Enter minute to see how many goals were scored before this minute: "))
    # If a non integer value is inputted, an error message shows:    
    except:
        print ("\033[4m\033[1mPlease enter an integer value\033[0m")
    # If both values inputted are integers, the code will run:       
    else: 
        with open('PremierLeagueMD4.csv', "r", newline='') as f:
            fr = csv.reader(f)
            count = 0

            for goal_minute in fr:
                # Loop through columns 4 through 13 to count the goals scored
                for index in range (4,13):
                    if goal_minute [index] == "NULL":
                        break
                    elif int(float(goal_minute [index])) >= begin_minute and int(float(goal_minute [index])) <= end_minute :
                        count = count + 1
            print (count, "goals were scored between minute", str(begin_minute) + "'", "and minute", str(end_minute) + "'")
        

#If option 2 is chosen, the program takes one time intervals and counts how many goals were scored after this minute
elif start in ["option 2", "'option 2'", "2"]:
    try:
        minute = int(input("Enter minute to see how many goals were scored after this minute: "))
    # If the value inputted is not an integer, the code will display an error message:
    except:
        print ("\033[4m\033[1mPlease enter an integer value\033[0m")
    # If the value inputted is an integers, the code will run:
    else:
        with open('PremierLeagueMD4.csv', "r", newline='') as f:
            fr = csv.reader(f)
            count = 0

            for goal_minute in fr:
                # Loop through columns 4 through 13 to count the goals scored
                for index in range (4,13):
                    if goal_minute [index] == "NULL":
                        break
                    elif int(float(goal_minute [index])) >= minute:
                        count = count + 1
        print (count, "out of 30 goals were scored after", "minute", str(minute) + "'")

# If a wrong value is entered for the option pick, a error message will be displayed:                  
else: 
    print("ERROR: Please enter 'option 1' or 'option 2'")


# In[ ]:




