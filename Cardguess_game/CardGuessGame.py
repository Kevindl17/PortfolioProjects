#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import shelve

#Save constants into a variable
DBNAME = "cardguess"
PLAYED = "played_times"
PLAYED_DEFAULT = 0
FEWEST = "fewest_guesses"
FEWEST_DEFAULT = 100

print ("\033[4m\033[1mWelcome to the card guessing game!\033[0m")
with shelve.open (DBNAME) as db:
    played_times = db.get (PLAYED, PLAYED_DEFAULT)
    fewest_guesses = db.get (FEWEST, FEWEST_DEFAULT)



SUITS = ["DIAMONDS", "HEARTS", "CLUBS", "SPADES"]
suitchoice = random.choice(SUITS)

number = random.randint (1,13)

card_names = {'ace': 1, 'jack': 11, 'queen':12, 'king':13}

for i in range(2,11):
    card_names[str(i)] = i

guessCount = 0
print ("\033[4m\033[1mThis game has been played", played_times, "times")
print("Can you beat", fewest_guesses, "guesses?\033[0m")
print(suitchoice, number)

Guess_Suit = input("Start by guessing the Suit: (Diamonds, Hearts, Clubs or Spades) ")

guessCount = guessCount +1


#Guessing the card Suit
while True:
    try:
        Guess_Suit = Guess_Suit.upper()
        guessCount = guessCount + 1
        if Guess_Suit not in SUITS:
            print("\033[4m\033[1mThe suit you picked was invalid, please type: Diamonds, Hearts, Clubs or Spades!\033[4m\033[0m")
            Guess_Suit = input("Pick another one: ")        
            guessCount = guessCount + 1
            
        elif Guess_Suit == suitchoice:
            print ("\033[1mCorrect!\033[0m")
            break
        elif Guess_Suit != suitchoice:
            print("That was Wrong!")
            Guess_Suit = input("Guess the Suit again: ")
            guessCount = guessCount +1
    except:
        print("Please print a normal value")
        
#Guessing the card number
Guess_number = input("Now Guess the card number or name of the face card\n(1= ace, 11= jack, 12= queen, 13= king): ")
Guess_number = card_names.get(Guess_number.lower().strip())
guessCount = guessCount + 1
while True:
    try:
        if Guess_number is None:
            print("\033[4m\033[1mThe card you picked is invalid\033[0m")
            Guess_number = input("Pick another one: ")        
            Guess_number = card_names.get(Guess_number.lower().strip())
            guessCount = guessCount + 1
            
        elif Guess_number == number:
            print("\033[1mTHATS IT, YOU WON! YOU GOT IT IN", guessCount, "GUESSES.")
            #reopen shelve and store guesses
            with shelve.open(DBNAME) as db:
                db[PLAYED] = db.get(PLAYED, PLAYED_DEFAULT) + 1
                if guessCount < db.get(FEWEST, FEWEST_DEFAULT):
                    db[FEWEST] = guessCount
                    print("You broke the record!\033[0m")
                if guessCount > db.get(FEWEST, FEWEST_DEFAULT):
                    print("You didn't break the record! Try again!\033[0m")
            break
        else:
            print('Wrong')
            Guess_number = input("Pick another one: ")
            Guess_number = card_names.get(Guess_number.lower().strip())
            guessCount = guessCount + 1
    except:
        print("Please print a normal value")
print()
print("Thanks for playing this game with me!")


# In[ ]:




