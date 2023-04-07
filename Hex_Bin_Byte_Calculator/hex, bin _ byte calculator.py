#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Create a converter that can convert a string to hex or binary value, and an integer to the bytes value

start = input("What conversion do you want to do? Option 1: string to hex or binary, Option 2: Integer to bytes ")

#1 = String to hex or binary
# -*- coding: utf-8 -*-

if start in ["1", "Option 1", "option 1"]:
    text = input ("What string do you want to convert? ")
    start1 = input("Do you want to get the hex value, the binary value, or both? ")
    start1 = start1.upper()
#Making sure that the user inputs a correct value for start 1, otherwise displaying an error
    if start1 in ["HEX","BIN", "BINARY", "BOTH"]:
        #Calculate hex value
        if start1 in ["hex", "Hex","HEX"]:
            for c in text:
                a = ord(c)
                print(c, hex(a))
                
        #Calculate bin value
        elif start1 in ["bin", "Bin", "Binary", "binary", "BIN", "BINARY"]:
            for c in text:
                a = ord(c)
                print(c, bin(a))
        
        #Calculate both values
        elif start1 in ["both", "Both", "BOTH"]:
            for c in text:
                a = ord(c)
                print(c, "hex:",hex(a), "binary:", bin(a))
    #Error message for wrong input
    else:
        print("Please enter the word hex, binary, or both!")

            
#2 = Integer to Bytes 
elif start in ["2", "Option 2", "option 2"]:
    
    #Tests if the user has inputted an integer
    try:
        text2 = input("What integer do you want to convert?")
        input2 = input("Do you want a big-endian or little-endian collection of bytes? ")
        input2 = input2.upper()
        #If an integer is inputted, this will give the big-endian value
        if input2 in ["BIG", "BIG-ENDIAN", "BIG ENDIAN"]:             
            ntext = int(text2)
            big = ntext.to_bytes(4, byteorder='big')
            print(ntext, "is", big, "as big-endian")

        #If an integer is inputted, this will give the little-endian value    
        elif input2 in ["LITTLE", "LITTLE-ENDIAN", "LITTLE ENDIAN"]:
            ntext = int(text2)
            small = ntext.to_bytes(4, byteorder='little')
            print(ntext, "is", small, "as big-endian")
    #An error is displayed if the user doesn't enter an integer value
    except:
        print("Please enter an integer value!")


# In[ ]:





# In[ ]:




